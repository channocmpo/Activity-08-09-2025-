from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('new/', views.create_tweet, name='create_tweet'),
]