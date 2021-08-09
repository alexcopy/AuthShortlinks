import logging
import re
import string
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
import random
from urllib.parse import urlparse


def rnd_string(min_limit, max_limit):
    chars = string.ascii_letters.join(string.digits)
    str_range = random.randint(min_limit, max_limit)
    return ''.join(random.choice(chars) for i in range(str_range))
