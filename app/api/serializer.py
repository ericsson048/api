from app.models import UserProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'FirstName', 'LastName', 'Email', 'password')
        extra_kwargs = {
            'write_only': True,
            'style': {'input_type': 'password'}
        }

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            FirstName=validated_data['FirstName'],
            LastName=validated_data['LastName'],
            Email=validated_data['Email'],
            password=validated_data['password'],
        )
        return user
