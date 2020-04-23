#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'index.html', context)


def bad_request1(request, exception):
    context = {}
    return render(request, 'error.html', context)


def bad_request2(request, exception):
    context = {}
    return render(request, 'error.html', context)


def bad_request3(request, exception):
    context = {}
    return render(request, 'error.html', context)



			
