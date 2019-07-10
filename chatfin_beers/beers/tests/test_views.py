# SHOULD BE DONE IN FUTURE RELEASES
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import User
from ..serializers import UserRegistrationSerializer
from ..views import user_creation
from rest_framework.test import APIRequestFactory

# initialize the APIClient app
print('here')

class UserTest(TestCase):
    print()
    factory = APIRequestFactory()
    request = factory.post('/users/', {"User_Name": "Sandeep","Password": "Sandeep1"}, format='json')