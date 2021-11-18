from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.getmovie),
    path('<int:movie_pk>/', views.movie_detail),
    path('community/', views.getreview),
    path('community/<int:review_pk>/', views.review_detail),
]