from django.urls import path

from . import views


urlpatterns = [
    path('', views.Feed.as_view()),  # feed에 들어서면 get으로 보내기, post 코멘트 받기
]
