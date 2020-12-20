from django.contrib import admin
from todo_item.models import ItemModel


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'expare_date']
    list_filter = ['created', 'name', 'is_done', 'expare_date']
    search_fields = ['name', 'expare_date']


admin.site.register(ItemModel, ItemAdmin)
