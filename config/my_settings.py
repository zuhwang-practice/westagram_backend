# 시크릿 키를 만들어주는 코드가 있음 ! 상록님께 받깅.
SECRET_KEY = {
    'secret': 'lgh%1w1g0k#1w!yqx3v2hso^!ta(tb^7^@4&&^rht=2i1vyp%y',
} # 변수로 해도 되고 딕셔너리로 해도됨.

ALGORITHM = 'HS256'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'westagram',  # 데이터베이스 이름
        'USER': 'root',  # 유저 이름
        'PASSWORD': '880802hwang!!',  # 패스워드
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
# 데이터 베이스 또한 공개되면 좋지 않으니 셋팅을 따로 빼두고. settings.py에서 입포트 해서 쓴다.


