from django.db import models
from django.core import validators


class Menu(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField('creation date', auto_now_add=True)
    modified_at = models.DateTimeField('last modification date', auto_now=True)
    dishes_count = models.IntegerField(default=0, editable=False)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(
        decimal_places=2,
        max_digits=9,
        validators=[validators.MinValueValidator(0)]
    )
    preparation_time = models.DurationField()
    is_vegetarian = models.BooleanField()
    created_at = models.DateTimeField('creation date', auto_now_add=True)
    modified_at = models.DateTimeField('last modification date', auto_now=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'dishes'

    def __str__(self):
        return self.name
