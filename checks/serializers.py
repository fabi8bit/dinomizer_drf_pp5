from django.db import IntegrityError
from rest_framework import serializers
from .models import Check

class CheckSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Check
        fields = ['id', 'created_at', 'owner', 'asset_id']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail':'possible duplicate'
            })
