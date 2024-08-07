from django import template

register = template.Library()

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