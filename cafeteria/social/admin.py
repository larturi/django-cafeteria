from asyncore import read
from django.contrib import admin
from .models import Link


class SocialAdmin(admin.ModelAdmin):
    read_only_fields = ('created', 'updated')
    list_display = ('key', 'name', 'url')
    search_fields = ('name',)


admin.site.register(Link, SocialAdmin)
