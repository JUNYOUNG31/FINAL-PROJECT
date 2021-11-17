# from re import L
# from django.shortcuts import get_list_or_404, get_object_or_404
# from .models import Genre, Movie, Review, Comment, Director, Actor, PhotoTicket, Rate, RecommendAlgoScore
# from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer, CommentSerializer, PhotoTicketSerializer, RateSerializer, RecommendAlgoScoreSerializer, DirectorSerializer, ActorSerializer
# from django.db.models import F, Q
# from django.contrib.auth import get_user_model

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status

# import requests
# from decouple import config
# import random
# from django.db.models.aggregates import Sum
# from django.core.paginator import Paginator

# # 인증된 사용자만 사용할 수 있도록 하는 데코레이터
# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# User = get_user_model()

# # 영화
# @api_view(['POST'])
# def get_movies_db(request):
#     if request.data.get('nickname') == 'admin':
#         API_KEY = config('API_KEY')
#         for page in range(1, 21):
#             url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&page={page}&region=KR&language=ko'
#             req = requests.get(url).json()
#             for data in req.get('results'):
#                 # 이미 DB에 있는 영화면 정보를 업데이트
#                 if Movie.objects.filter(title=data.get('title')).exists():
#                     movie = Movie.objects.get(title=data.get('title'))
#                     movie.popularity = data.get('popularity')
#                     movie.tmdb_vote_sum = data.get('vote_average') * data.get('vote_count')
#                     movie.tmdb_vote_cnt = data.get('vote_count')
#                     movie.save()
#                 # DB에 없는 영화면 새로 생성
#                 else:
#                     movie = Movie.objects.create(
#                         tmdb_id = data.get('id'),
#                         title = data.get('title'),
#                         original_title = data.get('original_title'), 
#                         release_date = data.get('release_date'),
#                         popularity = data.get('popularity'),
#                         tmdb_vote_sum = float(data.get('vote_average')) * float(data.get('vote_count')),
#                         tmdb_vote_cnt = data.get('vote_count'),
#                         our_vote_sum = 0,
#                         our_vote_cnt = 0,
#                         overview = data.get('overview'),
#                         # poster_path는 받아온 데이터에 앞부분 URL을 제외한 이미지의 이름만이 들어있으므로 처리
#                         poster_path = 'https://image.tmdb.org/t/p/w500' + data.get('poster_path'),
#                     )
#                     for genre_id in data.get('genre_ids'):
#                         genre = Genre.objects.get(tmdb_genre_id=genre_id)
#                         genre.movies.add(movie)
