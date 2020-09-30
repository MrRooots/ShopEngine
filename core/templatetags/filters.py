from django import template

register = template.Library()

@register.filter(name='substract')
def substract(value, arg):
  return int(round(value - arg, 0))