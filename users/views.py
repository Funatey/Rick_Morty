from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializer import CustomUserSerializer, ChangeUserSerializer
from rest_framework.generics import RetrieveUpdateAPIView


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ChangeUserSerializer
    queryset = CustomUser.objects.all()