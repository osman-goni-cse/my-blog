from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('image_tag','title', 'description', 'add_date')
  search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
  list_display = ('title',)
  search_fields = ('title',)
  list_filter = ('cat',)
  list_per_page = 5

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)