from rest_framework import serializers
from .models import Asset
from checks.models import Check
from django.contrib.humanize.templatetags.humanize import naturaltime
from projects.models import Project


class AssetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    check_id = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    project_owner = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.created_at)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_check_id(self, obj):
        # user = self.context['request'].user
        check = Check.objects.filter(
            asset_id=obj.id
        ).first()
        return check.id if check else None

    def get_project_owner(self, obj):
        request = self.context['request']
        return request.user == obj.project_id.owner

    class Meta:
        model = Asset
        fields = [
            'id', 'owner', 'profile_id', 'profile_image', 'asset_name',
            'category', 'description', 'image', 'assetfile', 'created_at',
            'updated_at', 'project_id', 'project_owner', 'is_owner', 'check_id'
        ]
