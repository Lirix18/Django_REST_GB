from rest_framework.serializers import HyperlinkedModelSerializer
from .models import MyUser


class MyUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'birthday_year', 'email')
