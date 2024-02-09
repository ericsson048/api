from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.api.views import  UserProfileAV

router = DefaultRouter()
router.register('user-api', UserProfileAV)

urlpatterns = [
    path('', include(router.urls))
]
