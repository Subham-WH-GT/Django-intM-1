from django.urls import path , include
from chat.consumers import ChatConsumer,onetoone

websocket_urlpatterns=[
    # path("",ChatConsumer.as_asgi()),
    path("",onetoone.as_asgi()),
    path('<str:groupkaname>/',ChatConsumer.as_asgi()),
]