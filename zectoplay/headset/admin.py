from django.contrib import admin

from .models import *

class HeadsetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'time_add', 'is_placed')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'type')
    list_editable = ('is_placed',)
    list_filter = ('is_placed', 'time_add')

admin.site.register(Headset, HeadsetAdmin)

