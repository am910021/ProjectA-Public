import locale
from django.core.urlresolvers import reverse
from datetime import datetime
from django import template
register = template.Library()

@register.filter(name='delOneNumber')
def delOneNumber(data):
    data.pop(0)
    return ""

@register.filter(name='setClass')
def setClass(data):
    value = data[0]
    return "active" if value % 2==0 else "info"

@register.filter(name='setNumber')
def setNumber(data):
    value = data[0]
    return value+1

@register.filter(name='getID')
def getID(data):
    return data.id

@register.filter(name='getNumber')
def getNumber(data):
    return data.number

@register.filter(name='getTotalAmount')
def getTotalAmount(data):
    return "{:,.0f}".format(locale.atoi(str(data.totalAmount)))

@register.filter(name='getPayStatus')
def getPayStatus(data):
    html="""<a href={url} class={cls}>{text}</a>"""
    span="""<span class="{cls}">{text}</span>"""
    if data.paymentStatus==0:
        return html.format(cls="text-danger", text="前往付款", url=reverse("pay2go:pay", args=(data.id,)))
    if data.paymentStatus==1:
        return html.format(cls="text-danger", text="已取號未付款", url=reverse("pay2go:pay", args=(data.id,)))
    # paymentStatus=2
    return span.format(cls="text-success", text="已付款")

@register.filter(name='getStatus')
def getStatus(data):
    status = data.status
    if status==0:
        return "未處理"
    if status==1:
        return "處理中"
    if status==2:
        return "已配送"
    return data.status

@register.filter(name='getDate')
def getDate(data):
    return str(datetime.strftime(data.date, '%Y-%m-%d %H:%M:%S'))

