from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    """
    User Model
    Defines the attributes of a User
    """
    User_Name = models.CharField(max_length=255, default='Default')
    Password = models.CharField(max_length=255)
    Created_at = models.DateField(("Date"), default=datetime.date.today)
    Updated_at = models.DateTimeField(auto_now=True)

class Beer(models.Model):
    """
    Beer Model
    Defines the attributes of a Beer
    """
    Beer_Name = models.CharField(max_length=255, default='Default')
    IBU = models.IntegerField()
    Calories = models.IntegerField()
    ABV = models.IntegerField()
    Style = models.CharField(max_length=255)
    BreweryLocation = models.CharField(max_length=255)
    Created_User = models.CharField(max_length=255)
    Created_at = models.DateField(("Date"), default=datetime.date.today)
    Updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    """
    Review Model
    Defines the attributes of a Review
    """
    Beer_Name = models.CharField(max_length=255, default='Default')
    Aroma = models.IntegerField()
    Appearance = models.IntegerField()
    Taste = models.IntegerField()
    Overall = models.IntegerField(default=0)
    Created_User = models.CharField(max_length=255)
    Created_at = models.DateField(("Date"), default=datetime.date.today)
    Updated_at = models.DateTimeField(auto_now=True)

