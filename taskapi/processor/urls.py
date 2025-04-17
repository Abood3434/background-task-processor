from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageUploadViewSet

router = DefaultRouter()
router.register(r'uploads', ImageUploadViewSet)

urlpatterns = [
    path('', include(router.urls))
]