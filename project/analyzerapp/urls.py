# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_text,name='get_text')
]
