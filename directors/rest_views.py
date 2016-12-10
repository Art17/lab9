from .serializers import DirectorSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Director
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework import permissions
from django.contrib.auth.models import User


class DirectorsAPI(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        directors = Director.objects.all()
        if 'year' in request.GET:
            directors = directors.filter(year=request.GET['year'])
        if 'name' in request.GET:
            directors = directors.filter(name=request.GET['name'])
        if 'surname' in request.GET:
            directors = directors.filter(surname=request.GET['surname'])
        if 'score' in request.GET:
            directors = directors.filter(score=request.GET['score'])
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(api_view(['GET', 'PUT', 'DELETE']), name='dispatch')
class DirectorAPI(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        try:
            director = Director.objects.get(pk=pk)
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)

    def put(self, request, pk):
        if not request.user.has_perm('directors.can_delete'):
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            director = Director.objects.get(pk=pk)
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            director = Director.objects.get(pk=pk)
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UsersAPI(views.APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)
