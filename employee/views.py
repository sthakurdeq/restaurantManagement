from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


@method_decorator(csrf_exempt, name="dispatch")
class UserViewSet(viewsets.ModelViewSet):
    """
    Create a Users Accepts POST,GET
    return fields as per the UserSerializer
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "post"]

    def update(self, request, pk=None):
        # returns forbidden when PUT request
        response = {"message": "Update function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        # returns forbidden when PATCH request
        response = {"message": "Update function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        # returns forbidden when DELETE request
        response = {"message": "Delete function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)
