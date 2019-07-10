from rest_framework import serializers
from .models import User, Beer, Review

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("User_Name", "Password")

class BeersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        print(Beer)
        fields = ('Beer_Name','IBU', 'Calories', 'ABV', 'Style', 'BreweryLocation', 'Created_User', 'Created_at', 'Updated_at')

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        print(Review)
        fields = ('Beer_Name','Aroma', 'Appearance', 'Taste','Overall', 'Created_User', 'Created_at', 'Updated_at')