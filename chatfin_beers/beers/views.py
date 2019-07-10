from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User,Beer,Review
from .serializers import BeersSerializer
from .serializers import RateSerializer
from .serializers import UserRegistrationSerializer
from datetime import date

#Get current date
today = date.today()

#Check if user exist in the system. Below function code has been reused 3 times in this veiw
def check_user_exist(user):
    return User.objects.filter(User_Name=user).count()

#To create a User
@api_view(['POST'])
def user_creation(request):
    # insert a new record for a user
    if request.method == 'POST':
        data = {
            'User_Name': request.data.get('User_Name'),
            'Password': (request.data.get('Password'))
                }
        #Validation:Check if user already exist
        current_user = request.data.get('User_Name')
        count_user = check_user_exist(current_user)
        if count_user > 0:
            return Response("User %s already exist in Chatfin system" %current_user, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#To Create a Beer
@api_view(['GET', 'POST'])
def get_post_beers(request):
    # get all beers
    if request.method == 'GET':
        beers = Beer.objects.all()
        serializer = BeersSerializer(beers, many=True)
        return Response(serializer.data)
    # insert a new record for a beers
    if request.method == 'POST':
        data = {
            'Beer_Name': request.data.get('Beer_Name'),
            'IBU': request.data.get('IBU'),
            'Calories': int(request.data.get('Calories')),
            'ABV': request.data.get('ABV'),
            'Style': request.data.get('Style'),
            'BreweryLocation': request.data.get('BreweryLocation'),
            'Created_User': request.data.get('Created_User')
        }
        # Validation:Check if user exist in the chatfin system
        current_user = request.data.get('Created_User')
        count_user = check_user_exist(current_user)
        if count_user == 0:
            return Response("User %s Doesnot exist in the system" %current_user + "Please create user"
                            , status=status.HTTP_400_BAD_REQUEST)

        # Validation:Check if user has already created an beer today
        count_beer = Beer.objects.filter(Created_User=request.data.get('Created_User'),Created_at = today ).count()
        if count_beer > 0:
            return Response("Hi %s, you have already created a beer today, please try tomorrow" %current_user
                            , status=status.HTTP_400_BAD_REQUEST)

        serializer = BeersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#To Rate Beer
@api_view(['POST'])
def rate_beer(request):

   # insert a new record to rate a beers
    if request.method == 'POST':
            data = {
                'Beer_Name' : request.data.get('Beer_Name'),
                'Aroma': request.data.get('Aroma'),
                'Appearance': int(request.data.get('Appearance')),
                'Taste': request.data.get('Taste'),
                'Created_User': request.data.get('Created_User')
            }
            #Validation:Check if user exist in the chatfin system
            current_user = request.data.get('Created_User')
            count_user = check_user_exist(current_user)
            if count_user == 0:
                return Response("User Doesnot exist in the system", status=status.HTTP_400_BAD_REQUEST)

            # Validation:Check if the beer exist in chatfin system
            beer_exist = Beer.objects.filter(Beer_Name=request.data.get('Beer_Name')).count()
            if beer_exist == 0:
                return Response(
                    "Hi %s, This beer doesnot exist in chatfin system, please create it first!!" % (current_user),
                    status=status.HTTP_400_BAD_REQUEST)

            # Validation:Check if the user has already captured rating on this beer
            beer_count = Review.objects.filter(Created_User=request.data.get('Created_User'),
                                                Beer_Name=request.data.get('Beer_Name')).count()
            if beer_count > 0:
                return Response("Hi %s, you have already provided rating for this beer" % current_user,
                                status=status.HTTP_400_BAD_REQUEST)
            # Validation:Check Aroma, Apeearance and taste should be in range of 1-5
            aroma = int(request.data.get('Aroma'))
            if aroma not in range(1, 6):
                return Response("Hi %s, please check the rating you have entered. Aroma should be between 1 to 5"
                                % current_user, status=status.HTTP_400_BAD_REQUEST)

            appearance = int(request.data.get('Appearance'))
            if appearance not in range(1, 6):
                return Response("Hi %s, please check the rating you have entered. Appearance should be between 1 to 5"
                                % current_user, status=status.HTTP_400_BAD_REQUEST)
            taste = int(request.data.get('Taste'))
            if taste not in range(1, 11):
                return Response("Hi %s, please check the rating you have entered. Taste should be between 1 and 10"
                                % current_user,status=status.HTTP_400_BAD_REQUEST)

            serializer = RateSerializer(data=data)
            if serializer.is_valid():
                    serializer.save()
                    aroma = serializer.validated_data['Aroma']
                    appearance = serializer.validated_data['Appearance']
                    taste = serializer.validated_data['Taste']
                    beer_Name = serializer.validated_data['Beer_Name']
                    created_User = serializer.validated_data['Created_User']
                    overall = (aroma + appearance + taste)/3 #Taken average of rating can also use math module for this operation
                    serializer.save(Overall=overall, Beer_Name=beer_Name,Created_User=created_User)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#To View all the ratings for a Beer
@api_view(['GET'])
def get_beer_review(request, beer_name):
    # Validation:Check if beer is present
    beer_count = Beer.objects.filter(Beer_Name=beer_name).count()
    if beer_count == 0:
        return Response("Beer %s doesnot exist in Chatfin system. Please create the Beer" %beer_name,status=status.HTTP_404_NOT_FOUND)
    review_count = Review.objects.filter(Beer_Name=beer_name).count()
    # Validation:Check if any review for the beer is present
    if review_count == 0:
        return Response("Sorry no one has reviewed for beer %s yet. Please provide your review" %beer_name,status=status.HTTP_404_NOT_FOUND)
    rate = Review.objects.filter(Beer_Name=beer_name)
    # get review of a single beers
    serializer = RateSerializer(rate, many=True)
    return Response(serializer.data)


###########Extra step to delete a Beer . Not in requirement Doc / Please ignore
@api_view(['GET', 'DELETE'])
def get_delete_update_beers(request, pk):
    try:
        beers = Beer.objects.get(pk=pk)
    except Beer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single beers
    if request.method == 'GET':
        serializer = BeersSerializer(beers)
        return Response(serializer.data)
    # delete a single beers
    if request.method == 'DELETE':
        beers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
