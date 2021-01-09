from django.contrib import admin
from todo_item.models import ItemModel


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'list_model']
    list_filter = ['created', 'name', 'is_done', 'list_model']
    search_fields = ['name', 'list_model__name']


admin.site.register(ItemModel, ItemAdmin)
