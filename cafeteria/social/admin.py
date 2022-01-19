from asyncore import read
from django.contrib import admin
from .models import Link


class SocialAdmin(admin.ModelAdmin):
    read_only_fields = ('created', 'updated')
    list_display = ('key', 'name', 'url')
    search_fields = ('name',)

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Personal').exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')


admin.site.register(Link, SocialAdmin)
