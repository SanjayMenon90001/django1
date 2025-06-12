# Create your models here.
from django.db import models
from django.contrib import admin
from django import forms

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter item name',
                'class': 'custom-class',
                'maxlength': '50',
                'style': 'background-color: #f0f0f0;',  # Inline CSS
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must be a Gmail address.")
        return email

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
    list_display = ('id', 'name', 'email', 'description', 'created_at')
