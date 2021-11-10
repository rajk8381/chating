from django.urls import path,re_path
from .consumers import ChatConsumer

ws_patterns=[
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
]