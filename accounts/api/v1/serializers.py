from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

user_model = get_user_model()

class AccountSerializer(ModelSerializer):

    class Meta:
        model = user_model
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
            'date_joined'
        )
        extra_kwargs = {
            'password': { 'required': True, 'write_only': True },
            'date_joined': { 'read_only': True }
        }

    def create(self, validated_data):
        user = user_model.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user