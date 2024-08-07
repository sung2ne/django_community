from datetime import datetime
from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def change_name(value):
    if not value:
        return ""
    
    return value[0] + "*" * (len(value) - 1)

@register.filter
def is_new(value):
    if not isinstance(value, datetime):
        return False
    
    now = timezone.now()
    return value.date() == now.date()

@register.filter
def sub(value, arg):
    return value - arg

@register.simple_tag(takes_context=True)
def query_string(context, **kwargs):
    request = context["request"]
    updated = request.GET.copy()
    
    for key, value in kwargs.items():
        updated[key] = value

    return updated.urlencode()
