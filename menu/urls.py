from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'$',
        views.MenuList.as_view(),
        name='user_api_menu'
    ),
]
