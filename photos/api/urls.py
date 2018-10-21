from django.urls import path, include

urlpatterns = [
    path('v1/', include(('photos.api.v1.urls', 'photos-api-v1'), namespace='v1')),
]