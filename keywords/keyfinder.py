#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def run(url):

    try:
        headers = \
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, features='lxml')

        metas = soup.find_all('meta')
        temp = []
        for meta in metas:
            try:
                s = meta.attrs['content']

                if 'IE=Edge' in s or 'width=' in s or 'initial-scale' \
                    in s or 'device-width' in s or 'authenticity_token' \
                    in s or 'https' in s or 'http' in s or 'telephone' \
                    in s or '4CDoo' in s or 'portal' in s:
                    continue
                else:
                    if len(s) == 0:
                        continue
                    if len(s) == 2:
                        if 'HP' in s or 'en' in s or 'IN' in s:
                            continue
                    if len(s) == 3:
                        if 'yes' in s:
                            continue
                    temp.append(s.encode('ascii', 'ignore'
                                ).decode('ascii').split(','))
            except:

                pass

        temp2 = []
        for i in temp:
            for j in i:

                if len(j) > 40:
                    pass
                else:
                    try:
                        j = int(j.strip())
                    except:
                        temp2.append(j)

        temp2 = list(set(temp2))

        # print(temp2)

        return temp2
    except Exception as e:

        return {'error': str(e)}


# print(run('http://stratz.com'))
# print(run('https://www.dotabuff.com/'))

# https://www.gamesgames.com/,  https://www.agame.com/

			
