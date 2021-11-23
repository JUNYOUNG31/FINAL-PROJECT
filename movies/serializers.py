from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import Genre, Movie, Review, Comment

class MovieListSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = '__all__'
    
    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'genre_ids', 'overview', 'release_date', 
        'poster_path', 'vote_count', 'vote_average',
        )


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name')


class ReviewSerializer(serializers.ModelSerializer):

    # class MovieListSerializer(serializers.ModelSerializer):
        
    #     class Meta:
    #         model = Movie
    #         fields = ('pk', 'title',)

    # movie_title = MovieListSerializer(write_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        depth = 1
        read_only_fields = ('user', 'like_users')


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('pk', 'title', )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at')
        read_only_fields = ('review',)


class MovieRecommendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title',)