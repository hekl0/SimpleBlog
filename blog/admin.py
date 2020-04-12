from django.contrib import admin

from .models import Post, Comment, Like

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    search_fields = ('user', 'post')
    list_filter = ('user',)

admin.site.register(Like, LikeAdmin)