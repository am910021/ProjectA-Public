import os
import sys
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def setupDB():
    sys.argv.append("migrate")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


def createCode(num):
    n,l,u,s=0,0,0,0
    sp = (33,64,35,36,37,94,38,42,95,43,45,61)
    t=""
    i=0
    m = num//4
    while(True):
        r=random.randint(1,4)
        if r==1 and (n<m or i>0):
            n+=1
            t+=chr(random.randint(48,57))
        if r==2 and (l<m or i>0):
            l+=1
            t+=chr(random.randint(97,122))
        if r==3 and (u<m or i>0):
            u+=1
            t+=chr(random.randint(65,90))
        if r==4 and (s<m or i>0):
            s+=1
            t+=chr(sp[random.randint(0,11)])
        if n+l+u+s>=m*4:
            i+=1
        if n+l+u+s>=num:
            break
    return t

def setup():
    import django
    django.setup()
    from main.models import Setting
    from shop.models import Brand, Category, Item
    try:
        Setting.objects.get_or_create(name="key",c1=createCode(32))
        Setting.objects.get_or_create(name="category", isActive=True)
        Setting.objects.get_or_create(name="gmailAccount")
        Setting.objects.get_or_create(name="pay2go", c4="True")
        brand = Brand.objects.get_or_create(name="未分類",
                                    description="未分類",
                                    content="未分類", isActive=True)
        Category.objects.get_or_create(name="未分類",
                                    description="未分類",
                                    isActive=True, brand=brand)
        print(bcolors.OKBLUE + "\n 設定成功。 \n \n" + bcolors.ENDC)
    except Exception as e:
        s = str(e)
        print(bcolors.FAIL + "\n\n取消設定。 \n"  + bcolors.ENDC)
        print(e)
        if """does not exist""" in s:
            print(bcolors.FAIL + "資料庫有問題，請檢查。 \n"  + bcolors.ENDC)


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectA.settings')
    setupDB()
    print(bcolors.OKBLUE + "\n 啟動基本設定" + bcolors.ENDC)
    setup()