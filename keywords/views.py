#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import Keys
from  . import keyfinder
from json2html import *


def keyIndex(request):

    # Returns an index page

    context = {}
    return render(request, 'keywords/index.html', context)


def KeyFinder(request):

    # Retrieve meta tags from the website with the custom script keyfinder in the keyword root directory
    # Check the existing website tags stored in database and using filter those tags which are similar are than grouped
    # If url entered is for the first time than it is saved with url, its meta data.

    k = Keys.objects.all()
    url = request.GET['url']
    list_keys = keyfinder.run(url)

    score = {}
    url_match = {}
    json = {'Recommend Tags': {}, 'Associated Tags': {}, 'Tags': ''}

    if type(list_keys) == dict:
        json['Tags'] = ''.join(list(list_keys)) + ' - ' \
            + list_keys['error']
        asa = json2html.convert(json={'Error': json['Tags']},
                                table_attributes='id="info-table" class="table table-dark table-responsive w-100 d-block d-xl-table table-striped table-hover"'
                                )
        return JsonResponse({'errorCode': asa})
    else:
        json['Tags'] = list(set(list_keys))
    list_keys = set(list_keys)
    length = len(list_keys)
    cnt = 0
    for j in list_keys:
        try:
            tee = int(j.strip())
        except:
            tee = ''.join([i for i in j if not i.isdigit()])
        s = k.filter(key__contains=tee)
        if len(s) > 0:
            for i in s:
                if i.url != url and i.url + '/' != url and i.url != url \
                    + '/':
                    if j in json['Associated Tags']:
                        json['Associated Tags'][j].append(i.url)
                        json['Associated Tags'][j] = \
                            list(set(json['Associated Tags'][j]))
                    else:
                        json['Associated Tags'][j] = [i.url]

                    if i.url in score:
                        score[i.url] += 1
                    else:

                        score[i.url] = 1

                    if i.url in url_match:
                        url_match[i.url].append(j)
                    else:
                        url_match[i.url] = [j]
                else:
                    pass

        cnt += 1
        if length == cnt:
            try:
                for (o, p) in score.items():
                    if p >= 3:
                        if o not in json['Recommend Tags']:
                            tests = list(set(url_match[o]))
                            if len(tests) <= 2:
                                pass
                            else:
                                json['Recommend Tags'][o] = \
                                    {'Matched': [], 'Different': []}
                                i = k.filter(url__contains=o)[0]
                                temp = set(i.key.split(','))
                                temp1 = list_keys
                                Difference = list(temp - temp1)
                                json['Recommend Tags'][o]['Different'
                                        ] = Difference
                                json['Recommend Tags'][o]['Matched'] = \
                                    tests
                        else:
                            pass
                    else:

                        pass
            except Exception as e:

                # print(e)

                pass

    check = Keys.objects.all()

    flag = 0
    for i in check:
        if str(str(i.url).strip()) == url:
            flag = 1
            pass
        elif str(str(i.url).strip()) + '/' == url:
            flag = 1
            pass
        elif str(str(i.url).strip()) == url + '/':

            flag = 1
            pass

    if len(check) != 0 and flag == 0:
        entry = Keys()
        entry.url = url
        string = ','.join(list_keys)
        if len(string) >= 900:
            string = string[:900]
        else:
            pass

        entry.key = string
        entry.save()

    if len(check) == 0:
        entry = Keys()
        entry.url = url
        string = ','.join(list_keys)
        if len(string) >= 1000:
            string = string[:900]
        else:
            pass

        entry.key = string
        entry.save()
    else:

        pass

    # print({'recommend':recommend,'url_dict':url_dict, 'tags':",".join(list_keys)})

    if len(json['Recommend Tags']) == 0:
        json['Recommend Tags'] = ['None']
    if len(json['Associated Tags']) == 0:
        json['Associated Tags'] = ['None']

    # asa={'Recommend URL':recommend,'Similat Tag URL':url_dict, "Site's Tag":",".join(list_keys)}

    tagA = json2html.convert(json={'Tags': json['Tags']},
                             table_attributes='id="info-table" class="table table-dark table-responsive w-100 d-block d-xl-table table-striped"'
                             )
    tagR = json2html.convert(json=json['Recommend Tags'],
                             table_attributes='id="info-table" class="table table-dark table-responsive w-100 d-block d-xl-table table-striped"'
                             )
    tagS = \
        json2html.convert(json={'Associated Tags': json['Associated Tags'
                          ]},
                          table_attributes='id="info-table" class="table table-dark table-responsive w-100 d-block d-xl-table table-striped"'
                          )

    # print(json)

    return JsonResponse({'html': {'Tags': tagA, 'Recommend Tags': tagR,
                        'Associated Tags': tagS}})


my_app = 'keywords'


			
