import json # req.body에 받는 정보 변환

# from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse


from account.models import User, UserProfile
from .models import Comment, Feed, FeedComment

# Create your views here.


class Feed(View):
    # @login_required
    def get(self, req):
        print(req)
        # 데이터베이스에서 피드 가져와서 화면에 뿌릴 피드 객체만들기
        # 로그인이 됬는지 확인, 유저정보 확인!
        # 각각의 DB에서 
        # ! 관계가 있는 테이블은 조인해서 가져와야 한다.
        
        return JsonResponse({'message': '응답!'})

    def post(self, req):
        
        data = req.body # 바디 정보 담기
        return JsonResponse({'message': 'DB update'})
      
      
    # ? 로그인 한 뒤 화면에서 유저가 팔로잉 하는 피드가 보여야 한다.
    #   get으로 해야하는 건지 post로 해야 하는건지..? 
    def getFeedList(self):
        get_feed_list = Feed.get();
        print(get_feed_list)
        result = {
            # data안에 리스트>각 인덱스에 DB필드 &값 보내기
            'data': [
                {
                    'user_name': '?',
                    'user_image ': '?',
                    'imag_url':'?',
                    'content':'?',
                    'like':'?',
                    'create_at':'?',
                    'comments':[
                       {
                         'user_id':'',
                        'conmment_text':''
                        },
                       {
                        'user_id':'',
                        'conmment_text':''}
                      ],
                }
            ]
        }
        return result
      
      
      
class CommentView():
    # 뿌려줄 일은 없고, 받으면 comment 테이블에 데이터는 저장해야함.
    def post(self, req):
        token = req.headers.get('Authorization', None) # 해더에서 담긴 토큰 꺼내기
        data  = json.loads(req.body) # 바디 데이터 꺼내기
        