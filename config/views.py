from django.views import View
from django.http import HttpResponse
from django.shortcuts import render


class Index(View):
    def get(self, req):
        print('출력')
        print('리퀘스트_해더 : ', req.headers)
        return HttpResponse('출력되남요')
