from django.urls import path,include 
from chat import views 
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    # path("",views.chatPage,name="chat-page"),
    path("",views.chatPage,name="chat-page"),
    path('<str:group_name>/',views.groupchat,name="group-chat"),

    path("auth/login/", LoginView.as_view
         (template_name="loginpage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(template_name="loginpage.html"), name="logout-user"),
]