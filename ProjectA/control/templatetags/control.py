from django import template
register = template.Library()

@register.filter(name='brandName')
def brandName(value, data):
    return data[value].name

@register.filter(name='getID')
def getID(value, data):
    return data[value].id

@register.filter(name='brandContent')
def brandContent(value, data):
    return data[value].content

@register.filter(name='brandDescription')
def brandDescription(value, data):
    return data[value].description

@register.filter(name='setClass')
def setAvtive(value):
    return "active" if value % 2==0 else "info"

@register.filter(name='getStatus')
def getStatus(value, data):
    normal = """<span class='text-info'>正常</span>"""
    shelves = """<span class='text-danger'>下架</span>"""
    return normal if data[value].isActive else shelves

@register.filter(name='getBrand')
def getBrand(value, data):
    return data[value].brand.name

@register.filter(name='getImage')
def getImage(value, data):
    html = """<img src="https://dl.dropboxusercontent.com/s/{path}" style="width:60px">"""
    return html.format(path=data[value].image) if data[value].image!="" else "沒有圖片"

"""@register.filter(name='brand')
def brand(value,db):
    return db[value].name"""
