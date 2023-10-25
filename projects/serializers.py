from rest_framework import serializers
from projects.models import Project
from participants.models import Participant
from django.db.models import Count


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    participant_id = serializers.SerializerMethodField()
    participants = serializers.SerializerMethodField()

    def get_participants(self, obj):
        participants = Participant.objects.filter(
            project_id=obj.id).count()
        return participants

    def get_participant_id(self, obj):
        user = self.context['request'].user
        participant = Participant.objects.filter(
            owner=user,
            project_id=obj.id
            ).first()
        # print(participant)
        return participant.id if participant else None

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Project
        # fields = '__all__'
        fields = [
            'id', 'owner', 'profile_id', 'project_name', 'profile_image',
            'start_date', 'expected_end_date', 'updated_at',
            'content', 'image', 'is_owner', 'status', 'participant_id',
            'participants',
        ]
