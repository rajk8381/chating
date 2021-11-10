from django.shortcuts import render
from .models import Message
# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

def room(request,room_name=None):
    mydic={}
    messages =Message.objects.filter(room=room_name)[:10]
    username=request.GET.get('username','no user')
    mydic['username']=username
    mydic['room_name']=room_name
    mydic['messages']=messages

    return render(request, 'chat/room.html',mydic)

def chats_view(request):
    return render(request, 'chat/chats.html')