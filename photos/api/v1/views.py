from photos.models import Photo
from .serializers import PhotoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .paginations import ShortPageNumberPagination

class PhotoView(ModelViewSet):
    model = Photo
    serializer_class = PhotoSerializer
    pagination_class = ShortPageNumberPagination

    def get_queryset(self):
        queryset = Photo.objects.all()
        group_id = self.request.query_params.get('group')
        # Get records created by current user
        queryset = queryset.filter(owner=self.request.user)
        print(queryset)

        if group_id:
            # Filtering by group_id
            queryset = queryset.filter(group_id=group_id)

        return queryset