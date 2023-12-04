from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewPost, CommentForm, NewCategory
from .models import Post, Category
from django.db.models import Q
from taggit.models import Tag
from django.db.models import Count
from .context_processors import common_tags
from django.utils import timezone


class PostList(generic.ListView):
    """
    Displays a list of published blog posts in 'index.html' template.
    Retrieves posts with status=1 (published) from the database and
    orders them by creation date in descending order. Paginates the
    results, displaying 3 posts per page.
    """

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-date_published')
    template_name = 'index.html'
    paginate_by = 3


class AddPost(LoginRequiredMixin, View):
    """
    On GET request renders 'add_post.html' and passes a new instance form.
    If the form is valid, creates a new post using the form data,
    setting the slug field, Post object is then saved, and the view
    redirects the user to the post_detail. If the form is not valid,
    it creates a new instance of the NewPost and re-renders the add_post.html.
    """
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'add_post.html',
            {
                "posted": False,
                'form': NewPost()
            }
        )

    def post(self, request, *args, **kwargs):
        new_post = NewPost(request.POST, request.FILES)

        if new_post.is_valid():
            new_post.instance.author = request.user

            if "save_post" in request.POST:
                new_post.instance.status = '0'
                new_post.save()
                messages.success(request, 'Your post has been saved.')

                # Redirect to the draft_list page
                return HttpResponseRedirect(reverse('draft_list'))

            elif "publish_post" in request.POST:
                new_post.save()
                messages.success(request, 'Your post is awaiting approval')
                slug = new_post.instance.slug

                return HttpResponseRedirect(
                    reverse(
                        'post_detail',
                        kwargs={"slug": slug}
                    ))
        else:
            form = new_post

            return render(
                request,
                "add_post.html",
                {
                    "posted": True,
                    "form": form
                }
            )

        return HttpResponse("Invalid request")


class CategoryView(View):
    """
    Manages category creation and display.
    Get method renders the category creation form.
    The post method processes the form submission,
    saves a new category if valid, and displays
    appropriate messages, else it notifies the user
    and reloads the form.
    """
    model = Category
    template_name = 'category_detail.html'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(
            request,
            'category_detail.html',
            {
                'category_form': NewCategory(),
                'categories': categories,
            })

    def post(self, request, *args, **kwargs):
        category_form = NewCategory(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, 'Your new category has been added!')
            return HttpResponseRedirect(reverse('category_list'))
        else:
            categories = Category.objects.all()
            messages.warning(
                request,
                'Invalid input: Avoid using symbols or numbers.'
                )
            return render(
                request,
                'category_detail.html',
                {
                    'category_form': NewCategory(),
                    'categories': categories,
                })


class CategoryPosts(View):
    template_name = 'category_posts.html'

    def get(self, request, category_name, *args, **kwargs):
        category = get_object_or_404(Category, name=category_name)
        posts = Post.objects.filter(category=category, status=1)
        context = {
            'category': category,
            'posts': posts,
        }

        return render(request, self.template_name, context)


# It retrieves drafts belonging to the logged-in user
# with a status of 0 and renders them using the draft_list template.
@login_required
def draft_list(request):
    drafts = Post.objects.filter(author=request.user, status=0)
    return render(request, 'draft_list.html', {'drafts': drafts})


class EditDraft(View):
    """
    Retrieves a draft for editing and renders the 'edit_draft.html' template
    with the draft form. The post method handles form submission.
    If the form is valid, it either saves the draft or publishes it,
    depending on the button clicked.
    """
    def get(self, request, slug, *args, **kwargs):
        draft = get_object_or_404(Post, slug=slug, author=request.user)
        form = NewPost(instance=draft)
        return render(
            request, 'edit_draft.html',
            {
                'form': form,
                'draft': draft
            })

    def post(self, request, slug, *args, **kwargs):
        draft = get_object_or_404(Post, slug=slug, author=request.user)
        form = NewPost(request.POST, request.FILES, instance=draft)

        if 'publish_draft' in request.POST:
            return self.publish_draft(request, form, draft)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your draft has been saved.')
            return HttpResponseRedirect(reverse('draft_list'))

        return render(
            request,
            'edit_draft.html',
            {
                'form': form,
                'draft': draft

            })

    def publish_draft(self, request, form, draft):
        """
        If the form is valid and the publish_draft button is clicked,
        it updates the date_published field, saves the form,
        displays a success message, and redirects to the
        post detail view for the published post.
        """
        if form.is_valid() and 'publish_draft' in request.POST:
            form.instance.date_published = timezone.now()
            form.save()
            messages.success(request, 'Your post is awaiting approval.')
            slug = form.instance.slug
            return HttpResponseRedirect(
                reverse(
                    'post_detail',
                    kwargs={"slug": slug}
                    ))

        return render(
            request,
            'edit_draft.html',
            {
                'form': form,
                'draft': draft
            })


class DeleteDraft(View):
    """
    Retrieves the draft to be deleted and renders the delete_draft template.
    The post method deletes the draft and redirects to the draft list view.
    """
    def get(self, request, slug, *args, **kwargs):
        draft = get_object_or_404(
            Post, slug=slug, author=request.user, status=0
        )
        return render(
            request,
            'delete_draft.html',
            {
                'draft': draft
            })

    def post(self, request, slug, *args, **kwargs):
        draft = get_object_or_404(
            Post, slug=slug, author=request.user, status=0
        )
        draft.delete()
        return HttpResponseRedirect(
            reverse(
                'draft_list'
                ))


class EditPost(LoginRequiredMixin, View):
    """
    If user is authenticated can edit their blog posts.
    When a user accesses the edit post page for a specific slug,
    it retrieves the corresponding post. If the user submits the edit form,
    it validates the data. Upon validation, the post is updated,
    and the user is redirected to the home page and gets notified.
    """
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        form = NewPost(instance=post)
        context = {
            'form': form
        }
        return render(request, 'edit_post.html', context)

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        form = NewPost(request.POST, request.FILES, instance=post)

        if form.is_valid() and post.author == request.user:
            form.save()
            messages.success(request, 'Post Updated!')
            return redirect('home')
        else:
            messages.error(
                request, 'You are not authorized to edit this post.'
            )
        return redirect('home')


class DeletePost(LoginRequiredMixin, View):
    """
    If user is authenticated can delete their blog posts.
    When a user accesses the delete post page for a specific slug,
    it retrieves the corresponding post. If the user confirms the deletion,
    the post is deleted from the database, and the user is
    redirected to the home page and gets notified.
    """
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'delete_post.html', {'post': post})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.author == request.user:
            post.delete()
            messages.success(request, 'Post deleted successfully!')
        else:
            messages.error(
                request, 'You are not authorized to delete this post.'
            )
        return redirect('home')


class PostDetail(View):
    """
    Displays detailed view of a single blog post.
    Handles GET and POST requests.
    GET: Retrieves and displays a post with its comments and like status.
    POST: Processes submitted comments, updates post details,
    and displays updated post.
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        post_tags = post.tags.all()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        if post.author != self.request.user and post.status == 0:
            return redirect(reverse('home'))

        author_profile = post.author.profile

        return render(
                    request,
                    "post_detail.html",
                    {
                        "author_profile": author_profile,
                        "author_username": post.author.username,
                        "post": post,
                        "comments": comments,
                        "post_tags": post_tags,
                        "liked": liked,
                        "comment_form": CommentForm()
                    },
                )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            tags_input = request.POST.get("tags", "")
            if tags_input:
                post.tags.set(*tags_input.split(","))
                post.save()

            messages.success(request, 'Comment posted successfully!')
            return HttpResponseRedirect(
                reverse(
                    "post_detail",
                    args=[post.slug]
                ))

        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm(),
                "liked": liked
            },
        )


class Tagged(View):
    """
    # Tutorial to retrieve the class tagged
    # https://www.youtube.com/watch?v=pnFCdWQbryo
    """
    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        posts = Post.objects.filter(tags=tag, status=1)
        context = {
            'tag': tag,
            'posts': posts,
        }
        return render(request, 'tags_page.html', context)


class PostLike(View):
    """
    Handles user likes/unlikes for a specific blog post.
    Retrieves the post based on the provided slug and
    toggles the like status for the existent current user.
    Redirects the user back to the post's detail page after
    the like/unlike operation.
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, 'You unliked the post.')
        else:
            post.likes.add(request.user)
            messages.success(request, 'You liked the post.')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id, *args, **kwargs):
    """
    View to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(Post, slug=slug, status=1)
    comment = get_object_or_404(post.comments, id=comment_id)

    if comment.name == request.user.username:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_edit(request, slug, comment_id, *args, **kwargs):
    """
    View to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = post.comments.filter(id=comment_id).first()

        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.name == request.user.username:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class SearchResults(View):
    """
    Custom view for displaying search results.
    # Tutorial to retrieve search term available at
    # https://www.youtube.com/watch?v=AGtae4L5BbI
    # Tutorial to retrieve common tags available at
    # https://www.youtube.com/watch?v=pnFCdWQbryo
    # counting common number of tags
    # https://stackoverflow.com/questions/1895638/django-tagging-count-and-ordering-top-tags-is-there-a-cleaner-solution-to-m
    # https://docs.djangoproject.com/en/dev/topics/db/aggregation/#filter-and-exclude
    """

    def post(self, request, *args, **kwargs):
        searched = request.POST['searched']
        posts = Post.objects.filter(
            Q(title__icontains=searched) |
            Q(author__username__icontains=searched) |
            Q(category__name__icontains=searched) |
            Q(tags__name__icontains=searched),
            status=1
            ).distinct()

        common_tags = Tag.objects.annotate(
            num_posts=Count('taggit_taggeditem_items')).order_by(
            '-num_posts')[:4]

        return render(
            request,
            'search_results.html',
            {
                'searched': searched,
                'posts': posts,
                'common_tags': common_tags
            })

    def get(self, request, *args, **kwargs):
        common_tags = Tag.objects.annotate(num_posts=Count(
            'taggit_taggeditem_items')).order_by('-num_posts')[:4]
        return render(
            request,
            'search_results.html',
            {
                'common_tags': common_tags
            })


def about_me(request):
    return render(request, 'about_me.html')


def error_404_view(request, exception):
    """
    # we add the path to the 404.html file
    # https://www.geeksforgeeks.org/django-creating-a-404-error-page/
    """
    return render(request, '404.html')
