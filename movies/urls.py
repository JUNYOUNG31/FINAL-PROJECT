from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.getmovie),
    path('<int:movie_pk>/', views.movie_detail),
    path('community/', views.getreview),
    path('community/create/', views.create_review),
    path('community/<int:review_pk>/', views.review_update_delete),
]