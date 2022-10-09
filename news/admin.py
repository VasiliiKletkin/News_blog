from django.contrib import admin
from .models import New


class NewAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'tags', 'publish', 'author']
    list_filter = ['publish', ]
    list_editable = ['text',]
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(New, NewAdmin)
