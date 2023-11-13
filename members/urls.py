from . import views
from django.urls import path
from .views import Profile

urlpatterns = [
     path('profile/<str:profile>/', views.Profile.as_view(), name='profile'),
     path('edit_profile/', views.EditProfile.as_view(), name='edit_profile'),
]
