"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from .views import Index

urlpatterns = [
    
    # * 301 에러가 뜬다 ? === 엔드포인트 urls에 /를 확인하자!!
    
    # ! 루트에는 '/'가 붙어 있기 때문에 앞에는 '/'가 필요 없으며
    # ! 뒤에 '/'는 뭔가 계속 시작 될거란 인식때문에 쓰지 안흔ㄴ다?... ㅇ......그냥 뒤에 '/'는 쓰지마!
    
    path('', Index.as_view()),
    path('account', include('account.urls')),
    path('feed', include('feed.urls'))
]
