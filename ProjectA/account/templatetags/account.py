from datetime import datetime
from django import template
register = template.Library()

@register.filter(name='setClass')
def setClass(value):
    return "active" if value % 2==0 else "info"

@register.filter(name='setNumber')
def setNumber(value):
    return value+1


@register.filter(name='getID')
def getID(value, data):
    return data[value].id

@register.filter(name='getName')
def getName(value, data):
    return data[value].itemID.name

@register.filter(name='getCost')
def getCost(value, data):
    return data[value].itemID.cost

@register.filter(name='getQty')
def getQty(value, data):
    return data[value].qty

@register.filter(name='getSubtotal')
def getSubtotal(value, data):
    qty = data[value].qty
    cost = data[value].itemID.cost
    return qty*cost

@register.filter(name='getDate')
def getDate(value, data):
    return str(datetime.strftime(data[value].date, '%Y-%m-%d %H:%M:%S'))

@register.filter(name='getInventory')
def getInventory(value, data):
    if data[value].qty<=data[value].itemID.inventory:
        return """<span class="text-success">有</span>"""
    return """<span class="text-warning">不足</span>"""

