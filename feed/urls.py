from django.urls import path

from . import views

urlpatterns = [
    # 댓글 달을 피드의 id를 전달받자 
    path('', views.FeedView.as_view()),
    # path('/comment', views.CommentView.as_view()),
]
