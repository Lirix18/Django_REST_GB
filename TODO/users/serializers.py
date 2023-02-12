from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import MyUser


class MyUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'birthday_year', 'email')


class MyUserModelSerializerV2(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('is_superuser', 'is_staff')
