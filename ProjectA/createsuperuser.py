import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectA.settings')
import django
django.setup()
import getpass
import re
from pip._vendor.distlib.compat import raw_input
from account.models import User, UserProfile
from django.utils import timezone

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def create():
    try:
        while(True):
            username = raw_input("帳號: ")
            check = len(list(User.objects.filter(username=username)))
            if check==0:
                break
            print(bcolors.FAIL + "帳號已經被註冊 \n" + bcolors.ENDC)
        
        password = ""
        password2 = ""
        while(True):
            password = getpass.getpass("密碼: ")
            password2 = getpass.getpass("密碼（再一次）: ")
            if password==password2:
                break
            else:
                print(bcolors.FAIL + "密碼不一樣,重新輸入 \n"  + bcolors.ENDC)
                
        while(True):
            email = raw_input("電子郵件: ")
            
            if email_valid(email):
                break
            print(bcolors.FAIL + "請輸入正確的電子郵件"  + bcolors.ENDC)
        
        admin = User()
        admin.username = username
        admin.set_password(password)
        admin.email = email
        admin.is_superuser = True
        admin.is_staff = True
        admin.is_active = True
        admin.date_joined = timezone.now()
        admin.save()
        
        userProflie = UserProfile()
        userProflie.username = username
        userProflie.user = admin
        userProflie.save()
        print(bcolors.OKBLUE + "\n "+ username +"帳號建立成功 \n \n" + bcolors.ENDC)
    except:
        print(bcolors.FAIL + "\n\n 取消建立帳號 \n"  + bcolors.ENDC)

def email_valid(email):
    match = re.search(r'"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$"', email)
    if match:
        return True
    else:
        return False

if __name__ == '__main__':
    print(bcolors.OKBLUE + "\n 建立管理員帳號 \n \n" + bcolors.ENDC)
    create()