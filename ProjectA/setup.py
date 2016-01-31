import os
import sys

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


def setup():
    import django
    django.setup()
    from main.models import Setting
    from shop.models import Brand, Category, Item
    try:
        Setting.objects.get_or_create(name="category")
        Setting.objects.get_or_create(name="gmailAccount")
        Setting.objects.get_or_create(name="pay2go")
        brand = Brand.objects.create(name="未分類",
                                    description="未分類",
                                    content="未分類", isActive=True)
        Category.objects.create(name="未分類",
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