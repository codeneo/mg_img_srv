from django.urls import path, include
from rest_framework import routers
from .views import ImageGroupView

router = routers.DefaultRouter()
router.register('groups', ImageGroupView, 'ImageGroup')

urlpatterns = [
    path('', include(router.urls)),
]
