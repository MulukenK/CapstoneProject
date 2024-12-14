Authentication Setup for Social Media API

1. Authentication Method

We are using Token-Based Authentication provided by the Django Rest Framework (DRF). This method ensures that only authenticated users can interact with protected endpoints.


2. Steps to Implement Token-Based Authentication

Step 1: Install Django Rest Framework and DRF Token Authentication

Ensure you have the DRF package installed. Run the following command:

* pip install djangorestframework djangorestframework-simplejwt


Step 2: Update settings.py

Add 'rest_framework' and 'rest_framework.authtoken' to your INSTALLED_APPS:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]

Configure DRF to use Token Authentication:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}


Step 3: Create Tokens for Users

Run the following command to generate tokens for users:

python manage.py migrate
python manage.py createsuperuser  # Create a test user
python manage.py drf_create_token <username>


Alternatively, you can use DRF’s built-in token generation endpoint to create tokens dynamically.



Step 4: Implement Login and Token Generation

Add the following endpoint in your urls.py to allow users to obtain their tokens.

from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns = [
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]

3. Testing the Authentication

You can use Postman or curl to test the token-based authentication. Below are the steps:

Step 1: Obtain Token

Send a POST request to /api/token/ with the username and password:

Request:

POST /api/token/
Content-Type: application/json

{
    "username": "testuser",
    "password": "securepassword"
}

Response:

{
    "token": "123456abcdefg"
}

Step 2: Access Protected Endpoints

To access any protected endpoint, include the token in the Authorization header as a Bearer Token:

Request:

GET /feed/
Authorization: Token 123456abcdefg

Response:

[
    {
        "id": 1,
        "user": 3,
        "content": "A post from followed users",
        "created_at": "2024-01-01T00:00:00Z"
    }
]


4. How It Works
	•	Users authenticate by sending their credentials to the /api/token/ endpoint.
	•	If the credentials are valid, a token is returned.
	•	For subsequent requests, the client includes the token in the Authorization header as Token <token>.
	•	DRF’s TokenAuthentication validates the token and allows access to the protected endpoints.

5. Notes
	•	Ensure the TokenAuthentication is used in all protected views by applying IsAuthenticated permissions.
	•	Use the Django admin panel or DRF’s /api/token/ endpoint to create and manage tokens for users.


6. Example Protected View

Here’s an example of a protected view in views.py:

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "This is a protected endpoint!"})

To access this view, send:

GET /protected/
Authorization: Token 123456abcdefg



Conclusion

Token-Based Authentication secures your API endpoints and ensures only authenticated users can access protected resources. Using tools like Postman or curl, you can easily test the authentication flow.