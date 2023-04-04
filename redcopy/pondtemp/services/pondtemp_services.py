import urllib.parse

import requests
import re
import os

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
METERS_URL = os.environ.get('METERS_URL')
IMG_PER_PAGE = int(os.environ.get('IMG_PER_PAGE', 20))


def _headers():
    access_token = ACCESS_TOKEN
    headers = {'Authorization': 'Bearer ' + access_token, "Content-Type": "application/json"}
    return headers


def urljoin(*args):
    trailing_slash = '/' if args[-1].endswith('/') else ''
    return "/".join(map(lambda x: str(x).strip('/'), args)) + trailing_slash


def _json_page(slug, query='', page=1, limit=IMG_PER_PAGE):
    try:
        page_url = os.environ.get('REMOTE_URL')
        if not query == '':
            query = 'q=' + query
        paging = "?%s&page=%d&limit=%d" % (query, page, limit)
        headers = _headers()
        url = urljoin(page_url, slug, paging)

        print(' REQUEST URL is:', url)
        r = requests.get(url, headers=headers)
        if not r.status_code == 200:
            raise Exception("return code is not 200 " + r.text)
        return r.json()
    except Exception as ex:
        print("Something wrong has happened with getpage ", ex)
        return {'pictures': '', 'error': ex}


def meter_index():
    pass


def all_cams_index():
    struct_data = _json_page('allfiles')
    return struct_data


def single_cam_details(request):
    try:
        slug = request.path_info.replace('pondtemp', '', 1)
        stats_type = request.GET.get("q")
        limit = int(request.GET.get("limit", IMG_PER_PAGE))

        path_info = request.GET.get("subcat", request.GET.get("folder"))
        subcat = request.GET.get("subfolder", '')

        if not subcat == '':
            subcat = f"&subfolder={subcat}"

        page = int(request.GET.get("page", 1))
        sub_query = f"{stats_type}&folder={path_info}{subcat}"
        page_content = _json_page(slug, sub_query, page, limit)
        data = []

        for l in page_content['pictures']['data']:
            if not type(l) == dict:
                data.append(page_content['pictures']['data'][l])
            else:
                data.append(l)

        if not page_content:
            return {'data': '', 'pagination': ''}
        return {'data': data, 'pagination': page_content['pictures']}
    except Exception as ex:
        print(ex)
        return {'data': '', 'pagination': ''}


def single_cam_stats(request):
    try:
        slug = request.path_info.replace('pondtemp', '', 1)
        page = int(request.GET.get("page", 1))
        limit = int(request.GET.get("limit", 20))
        page_content = _json_page(slug, '', page=page, limit=limit)
        return {'data': page_content['result']['data'], 'pagination': page_content["result"]}
    except Exception as e:
        print(e)
        return {"data": "", 'pagination': ''}
