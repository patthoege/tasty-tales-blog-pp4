from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from blog.models import Post


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, related_name='profile'
        )
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    posted = models.ManyToManyField(
        Post, related_name='blog_posts', blank=True
        )

    def __str__(self):
        return str(self.user)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
