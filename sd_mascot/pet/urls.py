from django.urls import path
from .views import mascot_index, feed_mascot, play_with_mascot, get_mascot_state

urlpatterns = [
    path('', mascot_index, name='mascot_index'),
    path('feed/', feed_mascot, name='feed_mascot'),
    path('play/', play_with_mascot, name='play_with_mascot'),
    path('get_state/', get_mascot_state, name='get_mascot_state'),
]