from django.contrib import admin
from .models import Post, Comment, Category
from members.models import UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title', 'author', 'slug',
        'category', 'status', 'approved',
        'created_on'
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


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name')
    list_filter = ('user',)
    search_fields = ['bio', 'first_name', 'last_name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name',)
