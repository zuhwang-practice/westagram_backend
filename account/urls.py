from django.urls import path

# view 불러오기
from .views import SignIn, SignUp

urlpatterns = [
    # 후행슬래시 필요없다용~
    path('sign_in', SignIn.as_view()),
    path('sign_up', SignUp.as_view())
]
