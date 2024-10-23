from django.urls import path
from .views import pet_status, feed_pet, play_with_pet, get_pet_stats

urlpatterns = [
    path('', pet_status, name='pet_status'),
    path('feed/', feed_pet, name='feed_pet'),
    path('play/', play_with_pet, name='play_with_pet'),
    path('get_pet_stats/', get_pet_stats, name='get_pet_stats'),
]