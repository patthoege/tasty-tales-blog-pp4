from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title', 'slug',
        'status', 'created_on',
        'category', 'approved'
    )
    search_fields = ['title', 'content', 'category']
    list_filter = ('approved', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'ingredients', 'instructions',)
    actions = ['approve_post']

    def approve_post(self, request, queryset):
        queryset.update(approved=True, status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')
