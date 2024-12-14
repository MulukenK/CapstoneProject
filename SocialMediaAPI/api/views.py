from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, PostSerializer
from .models import Post, Follow
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication




User = get_user_model()

# User Registration View
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "id": user.id,
            "username": user.username,
            "token": token.key
        }, status=201)
    return Response(serializer.errors, status=400)

# Retrieve User Details
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request, id):
    try:
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    



# Create a Post
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    data = {
        "user": request.user.id,
        "content": request.data.get("content")
    }
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Retrieve User Posts
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_posts(request, id):
    posts = Post.objects.filter(user_id=id)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# View Feed (Posts from Followed Users)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_feed(request):
    following = request.user.following.all()  # Get followed users
    followed_user_ids = [follow.followed.id for follow in following]
    posts = Post.objects.filter(user_id__in=followed_user_ids).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)




# Follow a User
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, id):
    if request.user.id == id:
        return Response({"error": "You cannot follow yourself."}, status=400)
    try:
        Follow.objects.get(follower=request.user, followed_id=id)
        return Response({"error": "You are already following this user."}, status=400)
    except Follow.DoesNotExist:
        Follow.objects.create(follower=request.user, followed_id=id)
        return Response({"status": f"You are now following user {id}."})

# Unfollow a User
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, id):
    try:
        follow = Follow.objects.get(follower=request.user, followed_id=id)
        follow.delete()
        return Response({"status": f"You have unfollowed user {id}."})
    except Follow.DoesNotExist:
        return Response({"error": "You are not following this user."}, status=400)
    



class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({'token': token.key})
    


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_post(request):
    ...