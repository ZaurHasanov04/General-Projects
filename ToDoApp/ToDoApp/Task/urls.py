from django.urls import include, path
from .views import *

urlpatterns=[
    path('', MyTaskView.as_view(), name='task'),
    path('delete/<pk>', DeleteTask.as_view(), name='delete_task'),
    path('update/<pk>/', TaskUpdateView.as_view(), name = 'update_task'),
]