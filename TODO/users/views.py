from rest_framework.viewsets import ModelViewSet
from .models import MyUser
from .serializers import MyUserModelSerializer


class MyUserViewSet(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserModelSerializer
