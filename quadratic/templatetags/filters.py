from django import template

register = template.Library()


@register.filter(name='is_int')
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
