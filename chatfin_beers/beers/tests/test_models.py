# SHOULD BE DONE IN FUTURE RELEASES

from django.test import TestCase
from ..models import User, Beer, Review


class UserTest(TestCase):
    """ Test module for Puppy model """
    print('hello')
    def setUp(self):
        print('heko')
        User.objects.create(
            User_Name='Casper', Password='3')


