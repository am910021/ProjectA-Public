import locale
import datetime
from django import template
from django.core.urlresolvers import reverse
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

@register.filter(name='setMoney')
def setMoney(data):
    money = str(data)
    return "{:,.0f}".format(locale.atoi(money))

@register.filter(name='getImage')
def getImage(data):
    html = """<img src="https://dl.dropboxusercontent.com/s/{path}" class="list-img">"""
    return html.format(path=data.image) if data.image!="" else "沒有圖片"


@register.filter(name='getPayStatus')
def getPayStatus(data):
    span="""<span class="{cls}">{text}</span>"""
    if data.paymentStatus<2:
        return span.format(cls="text-danger", text="未付款")
    
    # paymentStatus=2
    return span.format(cls="text-success", text="已付款")

@register.filter(name='setNext')
def setNext(data):
    buttom="""
    <button type="button" onclick="nextStatus({id},{status})">{text}</button>
    """
    if data.status==0:
        text="移到處理中"
    elif data.status==1:
        text="移到配送中"
    elif data.status==2:
        text="移到已完成"
    else:
        return ""

    return buttom.format(id=data.id, status=data.status+1, text=text, url=reverse('control:order', args=(data.status+1,)))

@register.filter(name='getStatus')
def getStatus(data):
    status = data.status
    if status==0:
        return "未處理"
    elif status==1:
        return "處理中"
    elif status==2:
        return "配送中"
    elif status==3:
        return "已完成"
    return data.status

@register.filter(name='getDate')
def getDate(data):
    return str(datetime.datetime.strftime(data.date, '%Y-%m-%d %H:%M:%S'))

@register.filter(name='getShelfStatus')
def getShelfStatus(data):
    span = """<span class="{cls}">{text}</span>"""
    if data.inventory<=0:
        return span.format(cls="text-danger", text="缺貨")
    if not data.isActive:
        return span.format(cls="text-danger", text="下架中")
    return span.format(cls="text-success", text="正常")

@register.filter(name='getDeals')
def getDeals(data):
    if data.sp:
        return "是"
    return "否"

@register.filter(name='getNew')
def getNew(data):
    if data.new:
        return "是"
    return "否"