from django.urls import path, include
from rest_framework import routers
from .views import PhotoView

router = routers.DefaultRouter()
router.register('photos', PhotoView, 'Photo')

urlpatterns = [
    path('', include(router.urls)),
]
