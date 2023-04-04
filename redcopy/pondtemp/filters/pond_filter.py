import ast

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='pondtemp_filter')
@stringfilter
def pondtemp_filter(value: str):
    value = value.replace('pagination.next', 'Next')
    value = value.replace('pagination.previous', 'Prev')
    return value.replace('api/', 'pondtemp/')


@register.filter(name='cam_item')
def cam_item(dictionary: dict, look_key: str):
    try:
        dic_key = dictionary.get(look_key)
        return dic_key.get('folder')
    except Exception as ex:
        print(ex)
        return 'None'
