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
        # print(req.user)
        # req.user # 회원인증을 통해 리턴받은 해당 유저의 recode가 들어가 있당.
        # 로그인한 유저의 feed..가져와야 하는뎅 피드는 그냥 1개이니 그냥 뿌리기..
        feed_list = Feed.objects.select_related('user').all()
        # ? select_related(테이블병)를 연결한 상태라면 user테이블을 거치지 않고 user_profile 의 정보를 가져올 수 있다?
        
        
        result = []
        for li in feed_list:
            # li.user.user_name  # => hwang, bludeberry
            # li.comment.values() # =>  QuerySet[{...},{...}]
            # # ! 코멘트를 담자 예외처리 피료한겨?
            # comment = list(li.comment.all().only("user.user_name", "comment")) # 특정컬럼 가져오기
            # print('---------------')
            # print('아이디', li.id)
            # print('이름', li.user.user_name)
            # ! 만약 유저사진이 딱 1개일 경우 절대적으로, get()으로 하면 [0]인덱스로 접근하지 않아도 된다.
            # 여러게를 한번에 받아오는 방법알아보기, [0]으로 접근하는 방법 말고 다른 방법은 뭐가 있을지 알아보자.
            # print('유저사진주소',li.user.user_uniq_id.filter(user_id=li.user_id)[0].image_url) # 유저사진 들고오려는데.. 오케해야되는규!?
            # print('피드사진주소',li.image_url)
            # print('피드내용',li.content)
            # print('코멘트 내용인데?',li.comment)
            # 메니투매니 일때는..?? ...코멘트 단 유저와 코멘트내용을 가져와서 리스트로 담아야지~
            # print('---------------')
            def check_comment_value(comment):
                if not comment:
                    return []
                else:
                    pass
                  
            result.append({
                'id' : li.id,
                'author':li.user.user_name, # FK일 경우, models.py에서 지정한 컬럼이름과, 실제 대상 테이블의 컬럼명을 입력한다.
                'author_img': li.user.user_uniq_id.filter(user_id=li.user_id)[0].image_url,
                'image_url' :li.image_url, 
                'content': li.content,
                'like': li.like,
                'comment': check_comment_value(li.comment) # 리스트가 담기죠
            })
        
        return JsonResponse({'data' : result, 'user_name' : req.user.user_name }, status=200)
        
          
    
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
        # req.user # 로그인한 USER_NAME을 가져온다.
        # print(req.user)
        # data  = json.loads(req.body) # 바디 데이터 꺼내기 :: #! feed_id, text
        # row = Comment.objects.create(user=user_name, comment=data.comment)
        # row.save()
        
        
        return JsonResponse({'message':'음... 코뮁트으'}, status=200)
    
    @login_required
    def get(self, req):
        print(req.user)
        return JsonResponse({'message':'코멩트겟!', }, status=200)
    
    
        
        