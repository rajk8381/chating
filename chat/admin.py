from django.contrib import admin

# Register your models here.
from .models import Message
class MessageAdmin(admin.ModelAdmin):
    list_display = ['username','room','content','created_at']

admin.site.register(Message,MessageAdmin)