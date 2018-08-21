from django.db.models import Count
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from .models import Menu
from .serializers import MenuSerializer


class MenuList(generics.ListAPIView):
    queryset = Menu.objects.annotate(
        dishes_count=Count('dish')
    ).filter(dishes_count__gte=1)
    serializer_class = MenuSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('name')
