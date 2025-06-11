from rest_framework import serializers
from .models import Item
from rest_framework.validators import UniqueValidator

class ItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[UniqueValidator(queryset=Item.objects.all())])

    class Meta:
        model = Item
        fields = '__all__'
