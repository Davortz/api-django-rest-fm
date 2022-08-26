# from rest_framework.view import APIView
from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.api.serializers import UserSerializer
from apps.users.models import User
from rest_framework.decorators import api_view

@api_view(['GET'])
def user_api_view(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        user_serelizer = UserSerializer(users, many=True)
        return Response(user_serelizer.data)

# class UserApiView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         user_serelizer = UserSerializer(users, many=True)
#         return Response(user_serelizer.data)
