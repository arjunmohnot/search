#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.urls import path
from  . import views
urlpatterns = [path('', views.appSearch, name='appSearch'), path('form'
               , views.form, name='form'), path('playstore',
               views.playstore, name='playstore'), path('appstore',
               views.appstore, name='appstore')]

			
