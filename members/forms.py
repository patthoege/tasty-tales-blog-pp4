from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        template_name = 'profile.html'
        fields = (
            'profile_image',
            'first_name',
            'last_name',
            'bio',
        )