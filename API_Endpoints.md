Endpoint	Method	Description	Request Body / Params	Response
/users/	POST	Create a new user	{ "username": "user1", "password": "..." }	{ "id": 1, "username": "user1" }
/users/<id>/	GET	Retrieve a user’s profile	id in URL path	{ "id": 1, "username": "user1" }
/posts/	POST	Create a new post	{ "user_id": 1, "content": "Hello!" }	{ "id": 1, "user_id": 1, "content": "..." }
/posts/<id>/	GET	Retrieve details of a post	id in URL path	{ "id": 1, "content": "Hello!" }
/users/<id>/follow/	POST	Follow a user	id in URL path	{ "status": "You are now following user 2." }
/users/<id>/unfollow/	POST	Unfollow a user	id in URL path	{ "status": "You have unfollowed user 2." }
/feed/	GET	Retrieve posts from followed users	None	[ { "id": 1, "content": "..." } ]

1. Create a Post (POST /posts/):
     • Request: {
  "user_id": 1,
  "content": "This is my first post!"
}

    • Response:	{
  "id": 1,
  "user_id": 1,
  "content": "This is my first post!",
  "created_at": "2024-06-14T12:00:00Z"
}

2. Follow a User (POST /users/<id>/follow/):
	• Request: No body, id in URL (e.g., /users/2/follow/).
	• Response: {
  "status": "You are now following user 2."
}
	
