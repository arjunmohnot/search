#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from  . import apple
import play_scraper


def appSearch(request):
    context = {}

    # Returns an index page

    return render(request, 'app/index.html', context)


def form(request):
    context = {}

    # print(dict(request.GET))
    # print("OKAY")

    # Returns input box based on store selected

    val = dict(request.GET)['drop_val']
    if 'playstore' in val:
        return HttpResponse('1')
    elif 'appstore' in val:

        return HttpResponse('2')
    else:

        return HttpResponse('0')


def playstore(request):

    # Retrieve android app information from play_scraper

    context = {}
    val = dict(request.GET)['package_val']
    try:
        d = play_scraper.details(val[0])
    except Exception as e:

        # print(e)

        return JsonResponse({'error': str(e)})

    if len(d['description']) > 200:
        d['description'] = (d['description'])[:200] + ' ...'
    else:
        pass

    context = {
        'title': d['title'],
        'icon': d['icon'],
        'rating': float(d['score']),
        'reviews': d['reviews'],
        'description': d['description'],
        'author': d['developer'],
        'developerLink': d['developer_url'],
        'url': d['url'],
        'installs': 'Installs: ' + d['installs'],
        }

    return JsonResponse(context)


def appstore(request):

    # Retrieve apple app information from custom script apple in the app root directory

    (appName, appID) = dict(request.GET)['app_val[]']
    d = apple.appleInfo(appName.strip(), appID.strip())
    try:
        if len(d['description']) > 200:
            d['description'] = (d['description'])[:200] + ' ...'
        else:
            pass

        return JsonResponse(d)
    except Exception as e:

        return JsonResponse({'error': "App doesn't exist " + str(e)})


my_app = 'app'

			
