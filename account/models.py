from django.db import models
# Create your models here.

class User(models.Model):
    # PK, unique, AI 자동생성
    # 직접 지정 : id = models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)
    user_name   = models.CharField(max_length=50)
    password    = models.CharField(max_length=200)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    # * 지금 User테이블에서 userprofile이 역참조 되고 있다. 사용하기 불편쓰!!.. User가 Userprofile을 정참조하는것이 데이터 접근 이 용이하다.. 코드도 쉽공
    class Meta:
        db_table = 'users'

 
class UserProfile(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_uniq_id')
    # ! related_name은 역참조시 사용, 지정하지 않으면 기본 역참조는 테이블명소문자_set으로 역참조를 찾아간다.
    image_url   = models.CharField(max_length=300, null=True)
    description = models.CharField(max_length=100, null=True)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profile'


# 정참조(바라보는, fk) : select_related
# 역참조(바라봐지는, ...) :prefetch_related
# ! 테이블명소문자_set  >>> 기본 역참조 데이터를 가져오는 법
# ! 역참조의 경우 related_name을 설정한 컬럼의 경우 XX_set으로 접근하지 않는다.