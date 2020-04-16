import json, jwt

from account.models     import User
from config.my_settings import SECRET_KEY, ALGORITHM
 
from jwt.exceptions     import InvalidSignatureError #! 이거 뭐여?~ 에러발생시키는 거얍?

from django.http        import JsonResponse, HttpResponse

# config.utils.py에는 데코레이터를 넣어 사용하나.
def login_required(func): 
    print('데코레이터 접근')
    def wrapper(self, req, *args, **kwargs):
        print('해더 확인', req.headers)
        # ! 보통 딕셔너리의 값을 가져올때 2번인자로 None을 두고, 빈값 에러 나는 것을 방지한다.
        token = req.headers.get('Authorization', None) # 두번째 인자는 뭐지? 1번인자를 키로검색, 없으면 None을 가져와라!
        # req.headers['Authorization'] # headers딕셔너리의 값을 가져오는 건 같으나, 에러처리가 필요하다.
        if not token: # 토큰이 없으면
            print('토큰이 없네?')
            return JsonResponse({'message': 'LOGIN_REQUIRED'}, status=400)
          
        try :
            token = jwt.decode(token, SECRET_KEY['secret'], ALGORITHM) # jwt로 토큰을 복호화 한다
            user = User.objects.get(user_name=token['user_name']) # jwt에 들어있는 user_name의 값을 받는다.
            # token에 뭘 넣고 인코딩 했는지 확인하고, 들어있는 값을 꺼낸다.
            print('변수 user에 담긴 내용을 보자',user)
            req.user = user # ? 왜 req에 user를 넣는거지?
        
        # ! 에러처리는 실제로 500에러를 내본뒤 호출되는 에러 목록을 확인, 정의해준다!    
        except InvalidSignatureError: # 특정에러일때를 걸러주는 겨 ?
            JsonResponse({'message':'UNAUTHORIZED'}, status=401)
        
        return func(self, req, *args, **kwargs)        
      
    return wrapper