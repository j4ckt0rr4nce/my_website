from django.contrib import admin
from .models import Message, Contact, Comment, Blog


admin.site.register(Message)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Blog)
