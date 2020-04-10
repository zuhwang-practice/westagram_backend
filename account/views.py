import json  # 제이슨으로 변환할때 필요
import jwt

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse


# DB가져오기
from .models import User
# Create your views here.


class SignUp(View):
    def post(self, req):
        data = json.loads(req.body)
        # print('username -', data['user_name'])
        # print('password -', data['password'])
        user_name = data['user_name']
        password = data['password']
        # id = 6~12자 사이 영문 대소문자+ 숫자0-9 만가능
        # pw = 영문 대소문자+숫자 0-9+특수문자 ~!@#$%^&*_+?,. 최대 25자 가능
        # user_list = User.objects.all()  # 데이터테이블 전체 가저오기
        # for i in range(len(user_list)):  # 테이블 행 각각 가져오기
        # print(user_list[i].user_name)
        # print(user_list[i].password)

        if User.objects.filter(user_name=user_name).exists():
            return JsonResponse({'message': '사용할수 없는 아이디'}, status=400)
        else:
            User(user_name=user_name, password=password).save()
            # ! save()보다 create 사용하는 것을 추천한다
            # * 왜냐하면, create로 하면 테이블을 생성, 변수에 담아 쓸수 있다.
            # * 왜 그래야 하느냐? 쿼리 효율을 생각해야 한다. 한번 DB에 접근하면 비용이 발생한다.
            # * 만약 지금 저장한 데이터를 다시 불러서 로직을 짜야 한다면. get(), filter() 써야 하는데
            # * create로 변수를 담으면 DB에 접근할 필요없어 비용을 아낄수 있고,
            # * 귀찮음을 격지 않아도 된다(테이블 목록 가져와서 몇번 인덱스에 필드명 뭐시기 가져와라 같은..)
            return JsonResponse({'message': '성공'}, status=200)


class SignIn(View):
    # 로그인 로직
    def post(self, req):
        data = json.loads(req.body)
        user_name = data['user_name']
        password = data['password']

        user_info = User.objects.filter(user_name=user_name)
        # print('유저네임: ', user_info[0].user_name)
        print(bool(user_info))
        if user_info:  # 유저정보가 있을 때
            if user_info[0].user_name == user_name and user_info[0].password == password:
              # jwt로 encode하면 byte로 바뀐다 그래서 문자열로 변환하는 것이 필요하다. 변환은 decode('utf-8')을 통해 진행한다. .. 만약 디코드 안하고 응답보내면 500에러~~
                token = jwt.encode(
                    {'user_name': user_name}, 'SECRET', algorithm='HS256').decode('utf-8')
                return JsonResponse({'token': token}, status=200)
            else:
                return JsonResponse({'message': '비밀번호 틀림'}, status=400)
        else:
            return JsonResponse({'message': '없는 유저'}, status=400)

        # print(data['user_name'], data['password'])
    # ? try & except 를 어떻게 언제 쓰야할까
