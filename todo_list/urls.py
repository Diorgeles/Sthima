from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^', todo_list, name='todo_list'),
    url(r'^delete_item/$', item_delete, name='item_delete'),

]
