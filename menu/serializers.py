from rest_framework import serializers

from .models import Dish, Menu


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'price')


class MenuDetailSerializer(serializers.ModelSerializer):
    dish_set = DishSerializer(many=True)

    class Meta:
        model = Menu
        fields = ('id', 'name', 'description', 'created_at', 'dish_set')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'description')
