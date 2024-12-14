from django.urls import path
from . import views
from .views import CustomAuthToken

urlpatterns = [
    # User endpoints
    path('users/register/', views.register_user, name='register_user'),
    path('users/<int:id>/', views.get_user, name='get_user'),
    
    # Post endpoints
    path('posts/', views.create_post, name='create_post'),
    path('users/<int:id>/posts/', views.get_posts, name='get_posts'),
    path('feed/', views.view_feed, name='view_feed'),

    # Follow endpoints
    path('users/<int:id>/follow/', views.follow_user, name='follow_user'),
    path('users/<int:id>/unfollow/', views.unfollow_user, name='unfollow_user'),

     path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]


