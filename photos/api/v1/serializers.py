import re
from photos.models import Photo
from rest_framework.serializers import ModelSerializer, SerializerMethodField

class PhotoSerializer(ModelSerializer):

    location_url = SerializerMethodField('get_photo_url')

    def get_photo_url(self, obj):
        """
        Convert the file path to url.
        Currently a workaround. Fix it by getting the domain and protocol(optional).
        """
        request = self.context['request']
        return re.sub(r'api\/v\d+\/photos\/(\d+\/)?', '', request.build_absolute_uri(obj.location))

    class Meta:
        model = Photo
        fields = (
            'id',
            'owner',
            'group',
            'title',
            'tag',
            'description',
            'date_posted',
            'date_taken',
            'location',
            'location_url',
        )
        extra_kwargs = {
            'date_posted': { 'read_only': True },
        }