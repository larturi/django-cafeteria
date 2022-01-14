from asyncore import read
from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    read_only_fields = ('created', 'updated')
    list_display = ('title', 'created')
    search_fields = ('title',)
    list_filter = ('created',)
    date_hierarchy = 'created'


admin.site.register(Service, ServiceAdmin)
