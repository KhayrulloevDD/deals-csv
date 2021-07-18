from django.urls import path
from . import api


urlpatterns = [
    path('get_deals', api.get_deals, name='get_deals'),
    path('post_deals', api.post_deals, name='post_deals'),
]
