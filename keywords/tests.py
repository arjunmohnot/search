#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.test import TestCase
from . models import Keys


# Create your tests here.

class KeysModelTests(TestCase):

    def test_url(self):

        # Url should be valid

        test1 = Keys(key='tags,meta-tags,testing,app', url='not a url')
        self.assertIs(test1.check_url(), False)

    def test_tag(self):

        # Length should not be greater than 1000 words

        randomLongText = 'random Text' * 10000
        test2 = Keys(key=randomLongText,
                     url='https://arjun009.github.io/')
        self.assertIs(test2.tag_length(), False)

    def test_tag_url(self):

        # TEsting both tag,url at the same time

        test3 = Keys(key='tags,meta-tags,testing,app',
                     url='https://arjun009.github.io/')
        self.assertIs(test3.tag_length(), test3.check_url(), True)

        randomLongText = 'random Text' * 10000
        test4 = Keys(key=randomLongText, url='//arjun009.github.io///')
        self.assertIs(test4.tag_length(), test4.check_url(), False)

    def test_response(self):

        # Hitting the webpage

        response = self.client.get('/keyword/')
        self.assertEqual(response.status_code, 200)

    def test_response_API(self):

        # Hit the database with wrong url

        response = \
            self.client.get('/keyword/key?url=%3A%2F%2Farjun009.github.io%2F'
                            )

        # print(response,response.context,response.json())
        # self.assertEqual(response.status_code, 200)

        # checking for error json

        self.assertEqual(''.join(list(response.json().keys())),
                         'errorCode')



			
