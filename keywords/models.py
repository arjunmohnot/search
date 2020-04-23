#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from validator_collection import validators, checkers


# Create your models here.

class Keys(models.Model):

    # Site Url

    url = models.CharField(max_length=200)

    # Keys will be separted by commas

    key = models.CharField(max_length=1000)

    # Returns url against the id

    def __str__(self):
        return self.url

    # Check if url is valid

    def check_url(self):
        check = checkers.is_url(self.url)
        return check

    # Check if tag length is less than 1000

    def tag_length(self):

        if len(self.key) > 1000:
            return False
        else:
            return True



			
