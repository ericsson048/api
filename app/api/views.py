from app.models import UserProfile
from rest_framework import viewsets, filters
from app.api.serializer import UserProfileSerializer
from rest_framework.authentication import TokenAuthentication
from app.api.permissions import UpdateOwnProfile


class UserProfileAV(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields=('FirstName', 'Email',)
