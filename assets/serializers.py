from rest_framework import serializers
from .models import Asset, Project
from checks.models import Check


class AssetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    check_id = serializers.SerializerMethodField()
    

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_check_id(self, obj):
        user = self.context['request'].user
        project_id = obj.project_id.id
        project = Project.objects.get(pk=project_id)
        if project.owner == user:
            check = Check.objects.filter(
                owner=user,
                asset_id=obj.id
            ).first()
            return check.id if check else None
        return None

        

    class Meta:
        model = Asset
        fields = [
            'id', 'owner', 'asset_name', 'category', 'description',
            'image', 'project_id', 'is_owner', 'check_id'
        ]