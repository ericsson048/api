from app.models import UserProfile
from rest_framework import viewsets
from app.api.serializer import UserProfileSerializer


class UserProfileAV(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
