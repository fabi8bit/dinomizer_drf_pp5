from rest_framework import serializers
from .models import Asset, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project

class AssetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    project = ProjectSerializer(read_only=True, many=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Asset
        # fields = '__all__'
        fields = [
            'id', 'owner', 'asset_name', 'category', 'description',
            'image', 'project', 'is_owner'
        ]