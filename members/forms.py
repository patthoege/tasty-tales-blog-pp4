from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        template_name = 'profile.html'
        fields = (
            'first_name',
            'last_name',
            'profile_image',
            'bio',
            'posted',
        )