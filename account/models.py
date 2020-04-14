from django.db import models
# Create your models here.

class User(models.Model):
    # PK, unique, AI 자동생성
    # 직접 지정 : id = models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)

    user_name = models.CharField(max_length=50)
    password  = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'


class UserProfile(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_uniq_id')
    image_url   = models.CharField(max_length=300, null=True)
    description = models.CharField(max_length=100, null=True)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profile'
