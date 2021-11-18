from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.getmovie),
    path('<int:movie_pk>/', views.movie_detail),
]