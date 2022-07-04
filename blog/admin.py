from django.contrib import admin
from blog.models import Category, Post


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'status', 'publish_time')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'lead', 'body')
    list_filter = ('status', 'publish_time')
    raw_id_fields = ('author',)
