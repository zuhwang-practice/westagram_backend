import json, jwt

from account.models     import User
from config.my_settings import SECRET_KEY, ALGORITHM
 
from jwt.exceptions     import InvalidSignatureError #! 이거 뭐여?~ 에러발생시키는 거얍?

from django.http        import JsonResponse, HttpResponse

# config.utils.py에는 데코레이터를 넣어 사용하나.
def login_required(func): 
    def wrapper(self, req, *args, **kwargs):
        token = req.headers.get('Authorization', None) # 두번째 인자는 뭐지?
        
        if not token: # 토큰이 없으면
            return JsonResponse({'message': 'LOGIN_REQUIRED'}, status=400)
          
        try :
            token = jwt.decode(token, SECRET_KEY, ALGORITHM) # jwt로 토큰을 복호화 한다
            user = User.objects.get(user_name=token['user_name']) # jwt에 들어있는 user_name의 값을 받는다.
            # token에 뭘 넣고 인코딩 했는지 확인하고, 들어있는 값을 꺼낸다.
            print('변수 user에 담긴 내용을 보자',user)
            req.user = user # ? 왜 req에 user를 넣는거지?
            
        except InvalidSignatureError: # 특정에러일때를 걸러주는 겨 ?
            JsonResponse({'message':'UNAUTHORIZED'}, status=401)
            
        return wrapper