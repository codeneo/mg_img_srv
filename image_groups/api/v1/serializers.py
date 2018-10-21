from image_groups.models import ImageGroup
from rest_framework.serializers import ModelSerializer

class ImageGroupSerializer(ModelSerializer):

    class Meta:
        model = ImageGroup
        fields = (
            'id',
            'name',
            'description',
            'owner',
            'date_created',
            'users'
        )
        extra_kwargs = {
            'date_created': { 'read_only': True },
        }