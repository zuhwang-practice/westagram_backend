from django.urls import path

# view 불러오기
from .views import SignIn, SignUp

urlpatterns = [
    path('/sign_in', SignIn.as_view()),
    path('/sign_up', SignUp.as_view())
]
