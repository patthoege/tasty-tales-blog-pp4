from . import views
from django.urls import path
from .views import Profile

urlpatterns = [
     path('profile/<str:profile>/', views.Profile.as_view(), name='profile'),
]
