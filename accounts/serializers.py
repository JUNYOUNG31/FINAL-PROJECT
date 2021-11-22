from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

# article_comments, articles, comments, date_joined, email, first_name, 
# followers, followings, groups, id, is_active, is_staff, is_superuser, 
# last_login, last_name,
# like_reviews, logentry, password, reviews, user_permissions, username

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'


# class FollowSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = get_user_model()
#         fields = ('followed', 'count')