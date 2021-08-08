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


def allowed_protocols(url: str):
    parsed_url = urlparse(url)
    if parsed_url.scheme in ['http', 'https', 'ftp', 'fttps']:
        return True
    return False


def short_links(request):
    try:
        if request.method == 'POST' and allowed_protocols(request.POST.get('url', '')):
            url = request.POST.get('url', '')
            rnd_key = rnd_string(5, 5)
            slug_url = 'htttp://localhost' + "/" + rnd_key
            # dbconn.insert_data(rnd_key, url)
        else:
            msg = "provided URL's protocol isn't supported request is empty<br>  supported protocols are: "
            error_msg = "http(s) and ftp(s)"
            return render(request, 'error.html', {'error': msg, 'desc': error_msg, 'template': {}})
    except Exception as ex:
        logging.error(ex)
        return HttpResponseBadRequest("Something went very wrong please check")

    return render(request, 'short_urls.html',
                  {'html': slug_url, 'slug_url': slug_url, 'url': rnd_key, 'template': {}})
