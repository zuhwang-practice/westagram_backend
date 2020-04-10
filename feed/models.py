from django.db import models
from django.utils import timezone

# 모델불러오기
from account.models import User, UserProfile
# Create your models here.
# 피드
# 댓글


class Comment(models.Model):
    many_to_many = models.ManyToManyField(through='',)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE(), related_name='유저 넘버')
    comment = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Feed(models.Model):
    # 회원장보가 삭제될때 피드도 같이 삭제 될것잉가..응...!
    user = models.ForeignKey(
        User, on_delete=models.CASCADE(), related_name='유저넘버')
    user_profile = models.ForeignKey(
        UserProfile,  on_delete=models.PROTECT(), related_name='작성자프로필 유저사진,소개글')
    comment = ForeignKey(
        Comment, ond_delete=models.PROTECT(), related_name='댓글목록')
    image_url = models.CharField(max_length=300, verbose_name='피드사진')
    description = models.TextField(verbose_name='피드내용')
    like = models.IntegerField(verbose_name='좋아요수')  # 좋아요기능 없음으로 숫자 집넣깅!
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
