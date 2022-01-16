from re import search
from django.contrib import admin
from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    read_only_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    read_only_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    post_categories.short_description = "Categorias"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
