
import logging
import re
import string
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseBadRequest
import random
from pathlib import Path
# from shortlinks.models import ShortLinks

APP_PATH = Path(__file__).parent.absolute()
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [APP_PATH.joinpath("templates")],
    },
]

def _rnd_string(min_limit, max_limit):
    chars = string.ascii_letters.join(string.digits)
    str_range = random.randint(min_limit, max_limit)
    return ''.join(random.choice(chars) for i in range(str_range))

def short_links(request):
    try:
        if request.method == 'POST' and re.match(r"^(http|ftp)s?://", request.POST.get('url', '')):
            url = request.POST.get('url', '')
            rnd_key = _rnd_string(5, 5)
            slug_url = 'htttp://localhost' + "/" + rnd_key
            # dbconn.insert_data(rnd_key, url)
        elif request.method == 'GET':
            return render(request, 'short_urls.html', {'template': TEMPLATES})
        else:
            msg = "provided URL's protocol isn't supported request is empty<br>  supported protocols are: "
            error_msg = "http(s) and ftp(s)"
            return render(request, 'error.html', {'error': msg, 'desc': error_msg, 'template': TEMPLATES})
    except Exception as ex:
        logging.error(ex)
        return HttpResponseBadRequest("Something went very wrong please check")

    return render(request, 'short_urls.html',
                  {'html': slug_url, 'slug_url': slug_url, 'url': rnd_key, 'template': TEMPLATES})


def shorturl(request, key):
    if len(key) > 5:
        return ''

    url_pair = "" #dbconn.get_key_from_db(key)
    if request.method == 'GET' and len(url_pair) == 1:
        return redirect(url_pair[key])
    return redirect('index')