from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import Thread, ChatMessage

admin.site.register(ChatMessage)


class ChatMessage(admin.TabularInline):
    model = ChatMessage
# Register your models here.
class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessage]
    class Meta:
        model = Thread


admin.site.register(Thread, ThreadAdmin)