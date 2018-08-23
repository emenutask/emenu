from __future__ import unicode_literals

from django.test import TestCase

from ..models import Dish, Menu


class IncrementDishesCountTest(TestCase):
    def test_if_incremented_on_create(self):
        menu = Menu.objects.create(name='Summer specials', description='')
        self.assertEqual(menu.dishes_count, 0)
        Dish.objects.create(
            menu=menu,
            name='Lemonade',
            description='pieces of lemon, cucumber and mint served with ice',
            is_vegetarian=True,
            price=12,
            preparation_time='2:00'
        )
        self.assertEqual(menu.dishes_count, 1)

    def test_if_not_incremented_on_update(self):
        menu = Menu.objects.create(name='Summer specials', description='')
        dish = Dish.objects.create(
            menu=menu,
            name='Lemonade',
            description='pieces of lemon, cucumber and mint served with ice',
            is_vegetarian=True,
            price=12,
            preparation_time='2:00'
        )
        self.assertEqual(menu.dishes_count, 1)
        dish.price = 14
        dish.save()
        self.assertEqual(menu.dishes_count, 1)

    def test_if_decremented_on_delete(self):
        menu = Menu.objects.create(name='Summer specials', description='')
        dish = Dish.objects.create(
            menu=menu,
            name='Lemonade',
            description='pieces of lemon, cucumber and mint served with ice',
            is_vegetarian=True,
            price=12,
            preparation_time='2:00'
        )
        self.assertEqual(menu.dishes_count, 1)
        dish.delete()
        self.assertEqual(menu.dishes_count, 0)
