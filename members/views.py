from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import get_object_or_404, render
from cloudinary import CloudinaryImage
from django.contrib.auth.models import User
from .models import UserProfile
from blog.models import Post
from .forms import ProfileForm


class Profile(View):
    def get(self, request, profile, *args, **kwargs):
        get_user = User.objects.get(username=profile)

        if request.user == get_user:
            posted_recipes = Post.objects.filter(author=get_user)
        else:
            posted_recipes = Post.objects.filter(author=get_user, private=False)

        profile_image = CloudinaryImage().image(quality='auto', fetch_format='auto')

        return render(
            request,
            'profile.html',
            {
                'profile': get_user.profile,
                'posted_recipes': posted_recipes,
                'profile_image': profile_image
            },
        )