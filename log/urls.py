from django.urls import path
from . import views

app_name = 'log'

urlpatterns = [
    path('', views.top.as_view(), name='top'),
]
