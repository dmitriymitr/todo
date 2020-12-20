from django.contrib import admin
from todo_item.models import ItemModel


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'expare_date', 'list_model']
    list_filter = ['created', 'name', 'is_done', 'expare_date', 'list_model']
    search_fields = ['name', 'expare_date']


admin.site.register(ItemModel, ItemAdmin)
