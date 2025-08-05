from django.contrib import admin
from .models import CodePost, Comment

@admin.register(CodePost)
class CodePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'language', 'created_at')
    search_fields = ('title', 'author_name', 'language')
    list_filter = ('language', 'created_at')
    ordering = ('-created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'commenter_name', 'created_at')
    search_fields = ('commenter_name', 'comment_text')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
