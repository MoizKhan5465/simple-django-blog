from accounts import views
from django.urls import path


app_name = "accounts"   
urlpatterns=[
    path("register/",views.register,name="register"),
    path("",views.login_user,name="login"),
    path("logout/",views.logoutt,name="logout"),
]