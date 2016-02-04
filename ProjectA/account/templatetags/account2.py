import locale
from datetime import datetime
from django import template
register = template.Library()

@register.filter(name='delOneNumber')
def delOneNumber(data):
    data.pop(0)
    return ""

@register.filter(name='setClass')
def setClass(data):
    return "active" if data[0] % 2==0 else "info"

@register.filter(name='setNumber')
def setNumber(data):
    return data[0]+1

@register.filter(name='getID')
def getID(data):
    return data.id

@register.filter(name='getName')
def getName(data):
    return data.item.name

@register.filter(name='getCost')
def getCost(data):
    return data.item.cost

@register.filter(name='getQty')
def getQty(data):
    return data.qty

@register.filter(name='getSubtotal')
def getSubtotal(data):
    qty = data.qty
    cost = data.item.cost
    return qty*cost

@register.filter(name='getDate')
def getDate(data):
    return str(datetime.strftime(data.date, '%Y-%m-%d %H:%M:%S'))

@register.filter(name='setMoney')
def setMoney(data):
    money = str(data)
    return "{:,.0f}".format(locale.atoi(money))

@register.filter(name='getInventory')
def getInventory(data):
    if data.qty<=data.item.inventory:
        return """<span class="text-success">有</span>"""
    return """<span class="text-warning">不足</span>"""

@register.filter(name='getTotalAmount')
def getTotalAmount(data):
    total = 0
    for i in data:
        total+= i.qty*i.item.cost
    return total

@register.filter(name='getFormatDate')
def getFormatDate(date):
    return str(datetime.strftime(date, '%Y-%m-%d %H:%M:%S'))


