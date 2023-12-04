from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


User = get_user_model()

# https://stackoverflow.com/questions/36317816/relatedobjectdoesnotexist-user-has-no-userprofile
# https://stackoverflow.com/questions/61580144/django-create-profile-for-user-signal
# code to connect Profile database to User from tutorial at
# https://www.youtube.com/watch?v=W8MLlwvSS-U&t=1078s


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        from .models import UserProfile
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
