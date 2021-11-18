from django.http import response
from django.http.response import HttpResponse
from django.views.decorators.http import require_safe
from django.shortcuts import get_list_or_404
from rest_framework import serializers
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view

@api_view(['GET'])
@permission_classes([AllowAny])
def getreview(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)
