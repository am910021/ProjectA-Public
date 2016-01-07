from django import template
register = template.Library()

@register.filter(name='brandName')
def brandName(value, data):
    return data[value].name

@register.filter(name='brandID')
def brandID(value, data):
    return data[value].id

@register.filter(name='brandContent')
def brandContent(value, data):
    return data[value].content

@register.filter(name='brandDescription')
def brandDescription(value, data):
    return data[value].description

@register.filter(name='setAvtive')
def setAvtive(value):
    return "active" if value % 2==0 else "info"


"""@register.filter(name='brand')
def brand(value,db):
    return db[value].name"""
