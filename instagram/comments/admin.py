from django.contrib import admin

# Register your models here.
from .models import Comment

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["content","user",  "timestamp",]
    list_filter = [ "timestamp","user"]
    search_fields = ["content","user"]

admin.site.register(Comment,CommentModelAdmin)