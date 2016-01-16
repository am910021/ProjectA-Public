import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectA.settings')
import django
django.setup()
import getpass
import re
from pip._vendor.distlib.compat import raw_input
from main.models import Setting

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def setup():
    Setting.objects.get_or_create(name="category")



if __name__ == '__main__':
    print(bcolors.OKBLUE + "\n 啟動基本設定 \n \n" + bcolors.ENDC)
    setup()