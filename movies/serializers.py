from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import Genre, Movie, Review, Comment

# 배우
# class ActorSerializer(serializers.ModelSerializer):

#     class MovieSerializer(serializers.ModelSerializer):
        
#         class Meta:
#             model = Movie
#             fields = ('pk', 'title', )

#     movie = MovieSerializer(many=True, read_only=True)

#     class Meta:
#         model = Actor
#         fields = ('name', 'movie', )


# class ActorListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actor
#         fields = ('pk', 'name', )


# 영화
# class MovieSerializer(serializers.ModelSerializer):

#     class ActorSerializer(serializers.ModelSerializer):

#         class Meta:
#             model = Actor
#             fields = ('pk', 'name', )

#     class ReviewSerializer(serializers.ModelSerializer):

#         class Meta:
#             model = Review
#             fields = ('pk', 'title', )

#     actor = ActorSerializer(many=True, read_only=True)
#     review = ReviewSerializer(many=True, read_only=True)

#     actor_pks = serializers.ListField(write_only=True)

#     def create(self, validated_data):
#         actor_pks = validated_data.pop('actor_pks')
#         movie = Movie.objects.create(**validated_data)

#         for actor_pk in actor_pks:
#             movie.actor.add(actor_pk)

#         return movie

#     def update(self, movie, validated_data):
#         actor_pks = validated_data.pop('actor_pks')

#         for attr, value in validated_data.items():
#             setattr(movie, attr, value)
#             movie.save()

#         movie.actor.clear
#         for actor_pk in actor_pks:
#             movie.actor.add(actor_pk)

#         return movie

#     class Meta:
#         model = Movie
#         fields = ('pk', 'title', 'overview',
#          'release_date', 'poster_path', 'actor', 'review', 'actor_pks')


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'genre_ids', 'overview', 'release_date', 'poster_path', 'vote_count', 'vote_average')


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
        fields = ('title', 'content', 'movie_title', 'rank', 'created_at', 'updated_at',)
        # depth = 1
        read_only_fields = ('user',)


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('pk', 'title', )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at')
        read_only_fields = ('review',)