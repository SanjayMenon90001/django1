from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        min_length=3, validators=[UniqueValidator(queryset=Item.objects.all())]
    )

    class Meta:
        model = Item
        fields = "__all__"

    def validate_description(self, value):
        if not value or len(value.strip()) < 10:
            raise serializers.ValidationError(
                "Description must be at least 10 characters long."
            )
        return value

    def validate_email(self, value):
        if value and not value.endswith("@gmail.com"):
            raise serializers.ValidationError("Email must be a Gmail address.")
        return value
