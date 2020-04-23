#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Module uses BeautifulSoup to find an app information based on its appid, appname from apple.com. It first checks
availabilty of app in US than in IN if it is unable to find than it returns an error.
'''

from bs4 import BeautifulSoup
from lxml import html
import requests


def appleInfo(appName, idNo):
    try:
        headers = \
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'}
        link_url = \
            'https://apps.apple.com/us/app/{}/id{}'.format(appName,
                idNo)
        try:
            page = requests.get(link_url, headers=headers)
        except:

            # print("https://apps.apple.com/us/app/{}/id{}".format(appName,idNo))

            try:
                link_url = \
                    'https://apps.apple.com/in/app/{}/id{}'.format(appName,
                        idNo)
                page = requests.get(link_url, headers=headers)
            except Exception as e:
                return {'error': str(e)}

        tree = html.fromstring(page.content)

        context = {
            'title': '',
            'icon': '',
            'rating': '',
            'reviews': '',
            'description': '',
            'author': '',
            'developerLink': '',
            'url': '',
            }

        # //Description

        description = page.text.split('data-test-bidi>'
                )[1].split('<!----></div>')[0]
        description = BeautifulSoup(description, 'lxml').text
        context['description'] = description

        # print(description)

        # //Rating

        rating = \
            float(page.text.split('<span class="we-customer-ratings__averages__display">'
                  )[1].split('Ratings</div>')[0].split('</span'
                  )[0].strip())
        review = \
            page.text.split('<span class="we-customer-ratings__averages__display">'
                            )[1].split('Ratings</div>'
                )[0].split('medium-show">')[1].strip()
        context['rating'] = rating
        context['reviews'] = review

        # print(rating,review)

        # //Title

        title = \
            str(page.text.split('<h1 class="product-header__title app-header__title">'
                )[1].split('</h1>')[0].split('<span')[0]).strip()
        context['title'] = title

        # print(title)

        # //Image
        # Big

        imageUrl = \
            page.text.split('<source class="we-artwork__source" srcset="'
                            )[1].split(' 2x')[0].strip().split(','
                )[1].split(' 2x')[0].strip()
        context['icon'] = imageUrl

        # print(imageUrl)

        # Small
        # print(page.text.split('<source class="we-artwork__source" srcset="')[1].split(' 2x')[0].strip().split(",")[0].split(' 1x')[0].strip())

        # //url

        url = page.text.split('shoebox-ember-data-store>'
                              )[0].split('</script>'
                )[0].split('"author":')[1].split('"url":"'
                )[1].split('"}')[0]
        context['url'] = link_url
        context['developerLink'] = url

        # print(url)

        # //seller

        seller = page.text.split('"seller":"'
                                 )[1].split('","isSiriSupported"')[0]
        context['author'] = seller

        # print(seller)

        # print(context)

        return context
    except Exception as e:

         # print(e)

        return {'error': str(e)}



			
