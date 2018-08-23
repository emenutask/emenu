import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Dish, Menu


class MenuListTests(APITestCase):
    def test_list_menus(self):
        """
        Ensure we list only non-empty menus
        """
        menu_with_two_dishes = Menu.objects.create(
            name='Small menu',
            description=''
        )
        Dish.objects.create(
            menu=menu_with_two_dishes,
            name='First dish',
            description='nothing special',
            is_vegetarian=True,
            price=12,
            preparation_time='2:00'
        )
        Dish.objects.create(
            menu=menu_with_two_dishes,
            name='Second dish',
            description='nothing special',
            is_vegetarian=True,
            price=12,
            preparation_time='2:00'
        )
        menu_with_one_dish = Menu.objects.create(
            name='Even smaller menu',
            description=''
        )
        Dish.objects.create(
            menu=menu_with_one_dish,
            name='The only dish in this menu',
            description='nothing special',
            is_vegetarian=True,
            price=12,
            preparation_time='2:00'
        )
        menu_without_dishes = Menu.objects.create(
            name='Nonsense menu',
            description=''
        )

        url = reverse('menu_api')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(
            {
                'id': menu_with_one_dish.id,
                'name': menu_with_one_dish.name,
                'description': menu_with_one_dish.description
            },
            response.data['results']
        )
        self.assertIn(
            {
                'id': menu_with_two_dishes.id,
                'name': menu_with_two_dishes.name,
                'description': menu_with_two_dishes.description
            },
            response.data['results']
        )
        self.assertNotIn(
            {
                'id': menu_without_dishes.id,
                'name': menu_without_dishes.name,
                'description': menu_without_dishes.description
            },
            response.data['results']
        )


class MenuDetailTests(APITestCase):
    def test_retrieve_menu(self):
        """
        Ensure we retrieve menu
        """
        menu = Menu.objects.create(
            name='Small menu',
            description=''
        )
        dish1 = Dish.objects.create(
            menu=menu,
            name='Dish with meat',
            description='nothing special',
            is_vegetarian=False,
            price=28,
            preparation_time='28:00'
        )
        dish2 = Dish.objects.create(
            menu=menu,
            name='Vegetarian dish',
            description='nothing special',
            is_vegetarian=True,
            price=24,
            preparation_time='24:00'
        )

        url = reverse('menu_api_detail', kwargs={'pk': menu.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            {
                'id': menu.id,
                'name': 'Small menu',
                'description': '',
                'created_at': menu.created_at.isoformat()[:26] + 'Z',
                'dish_set': [
                    {
                        'id': dish2.id,
                        'name': 'Vegetarian dish',
                        'description': 'nothing special',
                        'price': '24.00'
                    },
                    {
                        'id': dish1.id,
                        'name': 'Dish with meat',
                        'description': 'nothing special',
                        'price': '28.00'
                    },
                ]
            },
            response.json()
        )
