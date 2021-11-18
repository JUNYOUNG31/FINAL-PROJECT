from django.http.response import HttpResponse
from django.views.decorators.http import require_safe
from .models import Movie
from .serializers import MovieListSerializer
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view

@api_view(['GET'])
@permission_classes([AllowAny])
def getmovie(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)