from rest_framework import serializers
from .models import Asset, Project


class AssetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
        
        

    class Meta:
        model = Asset
        fields = [
            'id', 'owner', 'asset_name', 'category', 'description',
            'image', 'project_id', 'is_owner'
        ]