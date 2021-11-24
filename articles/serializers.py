from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import Article, ArticleComment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('pk', 'title', )


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        depth = 1
        read_only_fields = ('user',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleComment
        fields = ('id', 'content', 'created_at', 'updated_at')
        read_only_fields = ('article',)