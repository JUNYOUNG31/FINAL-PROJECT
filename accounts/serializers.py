from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Review, Comment
from articles.models import Article, ArticleComment

# article_comments, articles, comments, date_joined, email, first_name, 
# followers, followings, groups, id, is_active, is_staff, is_superuser, 
# last_login, last_name,
# like_reviews, logentry, password, reviews, user_permissions, username

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('reviews', 'username', 'id', 'comments', 'password')


###리뷰###

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


###게시글###

class CommentsRelatedArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = ArticleComment
        fields = ['id', 'user', 'content', 'created_at', ]


class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comments = CommentsRelatedArticleSerializer(many=True)
    like_users = UserSerializer(many=True)
    class Meta:
        model = Article
        fields = ['id', 'user', 'title', 'content', 'created_at', 'updated_at', 'like_users', 'comments']


class UserReviewArticleSerializer(UserSerializer):
    reviews = ReviewListSerializer(many=True)
    like_reviews = ReviewListSerializer(many=True)
    comments = CommentsRelatedReviewSerializer(many=True)

    articles = ArticleListSerializer(many=True)
    like_articles = ArticleListSerializer(many=True)
    article_comments = CommentsRelatedArticleSerializer(many=True)
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('reviews', 'like_reviews', 'comments', 
                                                'articles', 'like_articles', 'article_comments',)



# class UserArticleSerializer(UserSerializer):
#     articles = ArticleListSerializer(many=True)
#     like_articles = ArticleListSerializer(many=True)
#     comments = CommentsRelatedArticleSerializer(many=True)
#     class Meta(UserSerializer.Meta):
#         fields = UserSerializer.Meta.fields + ('articles', 'like_articles', 'comments')