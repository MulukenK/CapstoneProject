from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):  # Extending the built-in User model
    created_at = models.DateTimeField(auto_now_add=True)

# Post Model
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Follow Model
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)