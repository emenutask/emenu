from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^$',
        views.MenuList.as_view(),
        name='menu_api'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        views.MenuDetail.as_view(),
        name='menu_api_detail'
    ),
]
