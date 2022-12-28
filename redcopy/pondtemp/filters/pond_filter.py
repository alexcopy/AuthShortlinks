from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='pondtemp_filter')
@stringfilter
def pondtemp_filter(value: str):
    value = value.replace('pagination.next', 'Next')
    value = value.replace('pagination.previous', 'Prev')
    return value.replace('api/', 'pondtemp/')

