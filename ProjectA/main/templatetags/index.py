from django import template
register = template.Library()

@register.filter(name='delOneNumber')
def delOneNumber(data):
    data.pop(0)
    return ""

@register.filter(name='setClass')
def setClass(data):
    value = data[0]
    return "active" if value==0 else ""

@register.filter(name='setNumber')
def setNumber(data):
    value = data[0]
    return value