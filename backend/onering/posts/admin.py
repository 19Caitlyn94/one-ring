from django.contrib import admin
from .models import PostType

@admin.register(PostType)
class PostType(admin.ModelAdmin):
    fields = ('posttype_id', 'name', 'request_url')
    list_display = ('name', 'posttype_id')