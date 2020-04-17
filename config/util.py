import json, jwt

from account.models               import User
from config.my_settings           import SECRET_KEY, ALGORITHM
          
from jwt.exceptions               import InvalidSignatureError #! 이거 뭐여?~ 에러발생시키는 거얍?
          
from django.http                  import JsonResponse, HttpResponse
# from django.core.serializers.json import DjangoJSONEncoder



# config.utils.py에는 데코레이터를 넣어 사용하나.
def login_required(func): 
    print('데코레이터 접근')
    def wrapper(self, req, *args, **kwargs):
        # print(req.headers)
        print('다시이이이이이ㅣ', req.headers)
        print('해더 확인>>>>>>>>>>\n', req.headers.get('Authorization', None))
        # ! 보통 딕셔너리의 값을 가져올때 2번인자로 None을 두고, 빈값 에러 나는 것을 방지한다.
        # print(req.headers.get('Authorization'))
        token = req.headers.get('Authorization', None) # 두번째 인자는 뭐지? 1번인자를 키로검색, 없으면 None을 가져와라!
        # req.headers['Authorization'] # headers딕셔너리의 값을 가져오는 건 같으나, 에러처리가 필요하다.
        if not token: # 토큰이 없으면
            print('토큰이 없네?')
            return JsonResponse({'message': 'LOGIN_REQUIRED'}, status=400)
          
        try :
            token = jwt.decode(token, SECRET_KEY['secret'], algorithms=ALGORITHM) # jwt로 토큰을 복호화 한다
            user_info = User.objects.get(user_name=token['user_name']) # jwt에 들어있는 user_name의 값을 받는다.
            # DB 데이터 타입이 시간이 들어갈때 json 변환이 잘 되지 않는다. 이럴때 json.dumps를 사용한다.
            # user_info = json.dumps(user_info, cls=DjangoJSONEncoder)
            # token에 뭘 넣고 인코딩 했는지 확인하고, 들어있는 값을 꺼낸다.
            req.user = user_info # ? req 객체 안에 user키 를 생성, value 로 유저정보 넣어 리턴한다.
                   
        # ! 에러처리는 실제로 500에러를 내본뒤 호출되는 에러 목록을 확인, 정의해준다!    
        except InvalidSignatureError: # 특정에러일때를 걸러주는 겨 ?
            JsonResponse({'message':'UNAUTHORIZED'}, status=401)
        
        return func(self, req, *args, **kwargs)        
      
    return wrapper
  