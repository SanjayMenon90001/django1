from django.contrib import admin

from .models import Item  # Import your models here


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  # Show these fields in the list view
    search_fields = ("name",)  # Add a search box for 'name'
    list_filter = ("name",)  # Add a filter sidebar for 'name'


admin.site.register(Item, ItemAdmin)
