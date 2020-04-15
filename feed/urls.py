from django.urls import path

from . import views


urlpatterns = [
    # 댓글 달을 피드의 id를 전달받자 
    path('/feed', views.Feed.as_view()),
    path('/feed/comment', views.Comment.as_view()),
]
