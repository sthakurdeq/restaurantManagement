from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from restaurant.models import Ratings, Restaurant, Item, Menu
from restaurant.serializers import RatingSerializer, RestaurantSerializer, MenuSerializer, ItemSerializer


@method_decorator(csrf_exempt, name='dispatch')
class RestuarantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = RestaurantSerializer
    
    def update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    # def destroy(self, request, pk=None):
    #     response = {'message': 'Delete function is not offered in this path.'}
    #     return Response(response, status=status.HTTP_403_FORBIDDEN)

@method_decorator(csrf_exempt, name='dispatch')
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    # authentication_classes = [TokenAuthentication]
    serializer_class = MenuSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = MenuSerializer(queryset, many=True, fields=['id', 'restaurants', 'day', 'vote', 'items'])
        return Response(serializer.data)
@method_decorator(csrf_exempt, name='dispatch')
class TodayMenuViewSet(viewsets.ReadOnlyModelViewSet):
    # authentication_classes = [TokenAuthentication]
    today = datetime.today()
    day = {
        1 : "MON",
        2 : "TUE",
        3 : "WED",
        4 : "THUR",
        5 : "FRI",
    }
    weekday = datetime.now().weekday()
    queryset = Menu.objects.filter(created_at__year=today.year, created_at__month=today.month, created_at__day=today.day, day=day.get(weekday))
    serializer_class = MenuSerializer


@method_decorator(csrf_exempt, name='dispatch')
class ItemViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    def update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        response = {'message': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


@method_decorator(csrf_exempt, name='dispatch')
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingSerializer
    
    def update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        response = {'message': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)
