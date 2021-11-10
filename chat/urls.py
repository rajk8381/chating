from django.urls import path,include
from . import views
urlpatterns = [
    path('home/',views.index ),
    path('',views.chats_view ),
    path('<room_name>/',views.room, name='room'),

]
