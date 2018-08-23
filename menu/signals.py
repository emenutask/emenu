from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Dish


@receiver(post_save, sender=Dish, dispatch_uid='incrementing_dishes_count')
def increment_dishes_count(sender, instance, created, **kwargs):
    if created:
        menu = instance.menu
        menu.dishes_count += 1
        menu.save(update_fields=['dishes_count'])


@receiver(post_delete, sender=Dish, dispatch_uid='decrementing_dishes_count')
def decrement_dishes_count(sender, instance, **kwargs):
    menu = instance.menu
    menu.dishes_count -= 1
    menu.save(update_fields=['dishes_count'])
