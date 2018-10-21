from image_groups.models import ImageGroup
from .serializers import ImageGroupSerializer
from .paginations import ShortPageNumberPagination
from rest_framework.viewsets import ModelViewSet

class ImageGroupView(ModelViewSet):
    model = ImageGroup
    serializer_class = ImageGroupSerializer
    pagination_class = ShortPageNumberPagination

    def get_queryset(self):
        """
        Get ImageGroup instances where either the current_user is owner
        or part of users.
        """
        queryset = ImageGroup.objects.all()
        queryset = [ instance for instance in queryset \
                        if instance.owner == self.request.user or \
                        self.request.user in instance.users.all() ]
        return queryset