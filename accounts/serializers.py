from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Comment, Review

# article_comments, articles, comments, date_joined, email, first_name, 
# followers, followings, groups, id, is_active, is_staff, is_superuser, 
# last_login, last_name,
# like_reviews, logentry, password, reviews, user_permissions, username

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('reviews', 'username', 'id', 'comments', 'password')


class CommentsRelatedReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at', ]


class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comments = CommentsRelatedReviewSerializer(many=True)
    like_users = UserSerializer(many=True)
    class Meta:
        model = Review
        fields = ['id', 'movie_title', 'user', 'title', 'content', 'rank', 'created_at', 'updated_at', 'like_users', 'comments']


class UserReviewSerializer(UserSerializer):
    reviews = ReviewListSerializer(many=True)
    like_reviews = ReviewListSerializer(many=True)
    comments = CommentsRelatedReviewSerializer(many=True)
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('reviews', 'like_reviews', 'comments')