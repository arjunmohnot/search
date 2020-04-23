#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.test import TestCase


# Create your tests here.

class AppModelTests(TestCase):

    def test_view(self):

        # Hitting the webpage

        response = self.client.get('/appSearch/')
        self.assertEqual(response.status_code, 200)

    def test_view_dropdown(self):

        # Checking the dropdown

        # Play Store

        response1 = self.client.get('/appSearch/form?drop_val=playstore'
                                    )
        self.assertEqual(response1.status_code, 200)

        # App Store

        response2 = self.client.get('/appSearch/form?drop_val=appstore')
        self.assertEqual(response2.status_code, 200)

        # No Store Error

        response3 = self.client.get('/appSearch/form?drop_val=notlisted'
                                    )
        self.assertEqual(list(response3)[0].decode(), '0')

    def test_view_appInfo(self):

        # getting app info

        response1 = \
            self.client.get('/appSearch/playstore?package_val=com.optimisation.arjun.optimisation'
                            )
        self.assertEqual(response1.status_code, 200)

        response2 = \
            self.client.get('/appSearch/appstore?app_val%5B%5D=void-troopers-sci-fi-tapper&app_val%5B%5D=1367822033'
                            )
        self.assertEqual(response2.status_code, 200)

    def test_view_appInfo_error(self):

        # checking for error json

        response1 = \
            self.client.get('/appSearch/playstore?package_val=no.package.is.valid'
                            )
        self.assertEqual(''.join(list(response1.json().keys())), 'error'
                         )

        response2 = \
            self.client.get('/appSearch/appstore?app_val%5B%5D=com.optimisation.&app_val%5B%5D=check'
                            )
        self.assertEqual(''.join(list(response2.json().keys())), 'error'
                         )



			
