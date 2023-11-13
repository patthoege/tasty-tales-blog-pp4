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
        get_user = User.objects.get(username=profile)

        if request.user == get_user:
            posted_recipes = Post.objects.filter(author=get_user)
            user_posts = Post.objects.filter(author=get_user)
        else:
            posted_recipes = Post.objects.filter(author=get_user, approved=True)
            user_posts = Post.objects.filter(author=get_user, approved=True)

        profile_image = CloudinaryImage().image(quality='auto', fetch_format='auto')

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
        get_user = User.objects.get(id=request.user.id)
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

        