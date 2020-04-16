import json # req.body에 받는 정보 변환

from config.util  import login_required
# from django.shortcuts import render
from django.views import View
from django.http  import HttpResponse, JsonResponse


from account.models import User, UserProfile
from .models import Comment, Feed, FeedComment

# Create your views here.


class FeedView(View):
    @login_required
    def get(self, req):
        # 데이터베이스에서 피드 가져와서 화면에 뿌릴 피드 객체만들기
        # 로그인이 됬는지 확인, 유저정보 확인!
        # 각각의 DB에서 
        # ! 관계가 있는 테이블은 조인해서 가져와야 한다.
        # req.user # 회원인증을 통해 리턴받은 해당 유저의 recode가 들어가 있당.
        print(req.user) ## req.user에 있는 정보 확인
        
        # 로그인한 유저의 feed..가져와야 하는뎅 피드는 그냥 1개이니 그냥 뿌리기..
        feed_list = Feed.objects.all()
        # print(feed_list)
        print('여기까진 됭에', feed_list)
        result = []
        # for li in feed_list:
            # li.user.user_name  # => hwang, bludeberry
            # li.comment.values() # =>  QuerySet[{...},{...}]
            # ! 코멘트를 담자 예외처리 피료한겨?
            # comment = li.comment.all().only("user.user_name", "comment") # 특정컬럼 가져오기
            # print('---------------')
            # print('이름',li.user.user_name)
            # print('유저사진주소',li.user_profile)
            # print('피드사진주소',li.feed.image_url)
            # print('피드내용',li.feed.content)
            # print('---------------')
            # result.append({
            #     'author':li.user.user_name, # FK일 경우, models.py에서 지정한 컬럼이름과, 실제 대상 테이블의 컬럼명을 입력한다.
            #     'author_img':li.user_profile.image_url, # ? 이렇게 쓰는거야? 응 이렇게 쓰는겨 
            #     'image_url' :li.feed.image_url, 
            #     'content':li.feed.content,
            #     # 'comment': comment # 리스트가 담기죠
            # })
        
        return JsonResponse({'data' :result}, status=200)
        
          
    
    def post(self, req):
        data = req.body # 바디 정보 담기
        return JsonResponse({'message': 'DB update'}, status=200)
      
      
    # ? 로그인 한 뒤 화면에서 유저가 팔로잉 하는 피드가 보여야 한다.
    # result = {
        # data안에 리스트>각 인덱스에 DB필드 &값 보내기
        # 'data': [
        #     {
                # 'user_name': '?',
                # 'user_image ': '?',
                # 'imag_url':'?',
                # 'content':'?',
                # 'like':'?',
                # 'create_at':'?',
                # 'comments':[
                    # {
                      # 'user_id':'',
                    # 'conmment_text':''
                    # },
                    # {
                    # 'user_id':'',
                    # 'conmment_text':''}
                  # ],
            # }
        # ]
    # }
      
      
class CommentView():
    # 뿌려줄 일은 없고, 받으면 comment 테이블에 데이터는 저장해야함.
    @login_required
    def post(self, req):
        token = req.headers.get('Authorization', None) # 해더에서 담긴 토큰 꺼내기
        data  = json.loads(req.body) # 바디 데이터 꺼내기
        return JsonResponse({'message':'음... 코뮁트으'}, status=200)
        
        