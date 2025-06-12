# Create your models here.
from django.db import models
from django.contrib import admin

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(max_length=254, blank=True, null=True)
    
    def __str__(self):
        return self.name

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'description')  # <-- Add 'email' here
