from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import NewPost
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    """
    Displays a list of published blog posts in 'index.html' template.
    Retrieves posts with status=1 (published) from the database and
    orders them by creation date in descending order. Paginates the
    results, displaying 3 posts per page.
    """

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
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
        # queryset = Post.objects.filter(status=1)
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
            new_post.save()
            messages.success(request, 'Your post is awaiting approval')
            slug = new_post.instance.slug

            # Construct the URL using reverse and redirect to the post detail page
            post_detail_url = reverse('post_detail', kwargs={"slug": slug})
            return HttpResponseRedirect(post_detail_url)
            
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


class EditPost(View):
    """
    Handles editing existing blog posts.
    When a user accesses the edit post page for a specific slug,
    it retrieves the corresponding post. If the user submits the edit form,
    it validates the data. Upon validation, the post is updated,
    and the user is redirected to the home page.
    """
    def edit_post(request, slug):
        post = get_object_or_404(Post, slug=slug)
        if request.method == 'POST':
            form = NewPost(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post Updated!')
                return redirect('home')

        form =  NewPost(instance=post)
        context = {
            'form': form
        }
        return render(request, 'edit_post.html', context)

class DeletePost(View):
    """
    Handles deleting existing blog posts.
    When a user accesses the delete post page for a specific slug,
    it retrieves the corresponding post. If the user confirms the deletion,
    the post is deleted from the database, and the user is redirected to the home page.
    """
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'delete_post.html', {'post': post})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        messages.success(request, 'Post deleted successfully!')
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
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        if post.author != self.request.user and post.status == 0:
            return redirect(reverse('home'))

        return render(
                    request,
                    "post_detail.html",
                    {
                        "post": post,
                        "comments": comments,
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
            messages.success(request, 'Comment posted successfully!')
            return HttpResponseRedirect(reverse("post_detail", args=[post.slug]))

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
        else:
            post.likes.add(request.user)

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
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

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
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
