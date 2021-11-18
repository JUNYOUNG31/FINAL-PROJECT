from rest_framework import serializers
from .models import Review, Movie


class ReviewSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('pk', 'title', )

    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'title', 'rank', 'content', 'movie', )


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('pk', 'title', )
