from django.urls import path
from .views import index,add,remove

urlpatterns = [
    path('', index , name= 'index'),
    path('add/',add,name='add'),
    path('remove/',remove,name='remove'),
    path('remove/<int:ish_id>',remove,name='remove')
]
