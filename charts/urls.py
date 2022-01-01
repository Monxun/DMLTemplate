from django.urls import path
from . import views
from .api import api

app_name = 'charts'

urlpatterns = [
    path('', views.index, name='bar'),
    path('line/', views.line, name='linechart'),
    path('multi/', views.multi, name='multi'),
    path('api_v1/', api.urls), # Connects to api.py
]