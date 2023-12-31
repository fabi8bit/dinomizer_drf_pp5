from django.db import IntegrityError
from rest_framework import serializers
from .models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    participant_image = serializers.ReadOnlyField(
        source='owner.profile.image.url')
    participant_id = serializers.ReadOnlyField(source='owner.profile.id')
    project_name = serializers.ReadOnlyField(source='project_id.project_name')

    class Meta:
        model = Participant
        fields = [
            'id',
            'owner',
            'participant_image',
            'participant_id',
            'created_at',
            'project_id',
            'project_name'
            ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
