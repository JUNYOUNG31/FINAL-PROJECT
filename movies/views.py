from django.http import response
from django.http.response import HttpResponse
from django.views.decorators.http import require_safe
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import serializers
from .models import Movie, Review, Comment
from .serializers import (MovieListSerializer, ReviewListSerializer, 
ReviewSerializer, CommentSerializer)
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import api_view
from rest_framework import status

#전체 movie 목록 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def getmovie(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

#단일 영화 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieListSerializer(movie)
    return response(serializer.data)

# 전체 review 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def getreview(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

# 단일 review 생성
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_review(request):
    print(request.data)
    # movie = get_object_or_404(Movie, pk=pk)
    serializer = ReviewSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        print(serializer)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# def create_review(request):
#     serializer = ReviewSerializer(data=request.data)
#     # print(serializer.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# 단일 review 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        print(request.data)
        serializer = ReviewSerializer(review, data=request.data)
        print(serializer)
        if not request.user.reviews.filter(pk=review_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        if not request.user.reviews.filter(pk=review_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        review.delete()
        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)


# comment 목록 조회, 생성
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        comments = review.comment_set.order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 단일 comment 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, comment_pk, review_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        print(serializer)
        if not request.user.comments.filter(pk=comment_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        if not request.user.comments.filter(pk=comment_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        data = {
            'id': comment_pk,
            'delete': f'data {comment_pk} is deleted!!',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)