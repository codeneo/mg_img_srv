from django.urls import path, include

urlpatterns = [
    path('v1/', include(('image_groups.api.v1.urls', 'image-groups-api-v1'), namespace='v1')),
]