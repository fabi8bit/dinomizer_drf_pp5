# Create this serializer in order to add the profile_id  and profile_image to fields returned when  
# requesting logged in user’s details. we’ll know which profile to  
# link to and what image to show in the  navigation bar for a logged in user.
# we need then to overwrite the default USER_DETAILS_SERIALIZER in settings.py.


from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )