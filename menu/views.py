from rest_framework import generics
from rest_framework.filters import OrderingFilter

from .models import Menu
from .serializers import MenuDetailSerializer, MenuSerializer


class MenuList(generics.ListAPIView):
    queryset = Menu.objects.filter(dishes_count__gte=1)
    serializer_class = MenuSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('name', 'dishes_count')


class MenuDetail(generics.RetrieveAPIView):
    serializer_class = MenuDetailSerializer
    queryset = Menu.objects.filter(dishes_count__gte=1)
