#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [path('', views.keyIndex, name='keyIndex'), path('key',
               views.KeyFinder, name='KeyFinder')]

			
