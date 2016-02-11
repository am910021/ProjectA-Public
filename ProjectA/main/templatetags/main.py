from django import template
import datetime
register = template.Library()

@register.filter(name='getMMDD')
def getMMDD(data):
    return "("+str(datetime.datetime.strftime(data.date, '%m/%d'))+")"

@register.filter(name='getDate')
def getDate(data):
    return datetime.datetime.strftime(data.date, '%Y-%m-%d %H:%M:%S')