from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def duration_minutes(start, end):
    """
    Принимает два объекта datetime и возвращает разницу в минутах.
    """
    if start and end:
        delta = end - start
        return int(delta.total_seconds() / 60)
    return ''

@register.filter(name='replace')
@stringfilter
def replace(value, arg):
    """
    Заменяет подстроку в строке.
    Использование:
      {{ value|replace:"old,new" }}
    """
    try:
        old, new = arg.split(',')
    except ValueError:
        return value
    return value.replace(old, new)
