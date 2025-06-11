from rest_framework import serializers
from .models import Item
from rest_framework.validators import UniqueValidator

class ItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        min_length=3,
        validators=[UniqueValidator(queryset=Item.objects.all())]
    )

    class Meta:
        model = Item
        fields = '__all__'

    def validate_description(self, value):
        if not value or len(value.strip()) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters long.")
        return value
