from asyncore import read
from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    read_only_fields = ('created', 'updated')
    list_display = ('title',)
    search_fields = ('title',)


admin.site.register(Page, PageAdmin)
