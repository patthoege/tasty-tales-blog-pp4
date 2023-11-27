from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect, reverse
from cloudinary import CloudinaryImage
from django.contrib.auth.models import User
from .models import UserProfile
from blog.models import Post
from .forms import ProfileForm
from django.contrib import messages


class Profile(View):
    def get(self, request, profile, *args, **kwargs):
        get_user = get_object_or_404(User, username=profile)

        if request.user == get_user:
            posted_recipes = Post.objects.filter(author=get_user, status=1)
            user_posts = Post.objects.filter(author=get_user, status=1)
        else:
            posted_recipes = Post.objects.filter(author=get_user, approved=True, status=1)
            user_posts = Post.objects.filter(author=get_user, approved=True, status=1)


        profile_image = CloudinaryImage().image(quality='auto', fetch_format='auto')

        if not request.user.is_authenticated:
            # If the user is not authenticated, redirect them to the sign-up page
            return redirect(reverse('account_signup'))

        return render(
            request,
            'profile.html',
            {
                'profile': get_user.profile,
                'user_posts': user_posts,
                'posted_recipes': posted_recipes,
                'profile_image': profile_image,
            },
        )

class EditProfile(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # get_user = User.objects.get(id=request.user.id)
        get_user = get_object_or_404(User, id=request.user.id)
        profile_form = ProfileForm(instance=get_user.profile)

        return render(
                request,
                'edit_profile.html',
                {
                    'profile_form': profile_form,
                    'profile': get_user.profile,
                })
    def post(self, request, *args, **kwargs):
        get_user = User.objects.get(username=request.user)

        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=get_user.profile
            )

        if profile_form.is_valid():
            if 'clear_image' in request.POST: 
                get_user.profile.profile_image.delete()
                get_user.profile.profile_image = None
                get_user.profile.save()  
            else:
                profile_form.save()

            messages.success(request, 'Profile updated successfully.')
            recipes = Post.objects.filter(author=get_user)
            posted_recipes = Post.objects.filter(author=get_user)

            return redirect(
                reverse(
                    "profile",
                    kwargs={'profile': get_user.profile} 
                    ))
        else:
            messages.error(request, 'There was an error updating the profile. Please check the form.')
            return render(
                request,
                'edit_profile.html',
                {
                    'profile_form': profile_form,
                    'profile': get_user.profile,
                })