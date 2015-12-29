from main.views import BaseView
from shop.models import Type, Item
from django.contrib.auth.models import User
from account.models import UserProfile
from dropbox.client import DropboxOAuth2Flow, DropboxClient
from django.http import HttpResponseRedirect, HttpResponseForbidden,HttpResponse

class CShop(BaseView):
    template_name = 'shop/detail.html'
    page_title = '商店'
    
    def get(self, request, *args, **kwargs):
        print("aaaaaaaaaaaaaaaaaaaaaaa")
        print(request.get_host())
        print(dropbox_auth_start(request))
        print(dropbox_auth_finish(request))
        kwargs['find'] = True
        return super(CShop, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(CShop, self).post(request, *args, **kwargs)

def get_dropbox_auth_flow(request):
    redirect_uri = "http://localhost/shop"
    return DropboxOAuth2Flow('', '', redirect_uri, request.session, "dropbox-auth-csrf-token")

# URL handler for /dropbox-auth-start
def dropbox_auth_start(request):
    authorize_url = get_dropbox_auth_flow(request).start()
    return HttpResponseRedirect(authorize_url)

# URL handler for /dropbox-auth-finish
def dropbox_auth_finish(request):
    try:
        access_token, user_id, url_state = get_dropbox_auth_flow(request).finish(request.GET)
    except DropboxOAuth2Flow.BadRequestException as e:
        return HttpResponse(status=204)
    except DropboxOAuth2Flow.BadStateException as e:
        # Start the auth flow again.
        return HttpResponseRedirect("http://localhost/dropbox_auth_start")
    except DropboxOAuth2Flow.CsrfException as e:
        return HttpResponseForbidden()
    except DropboxOAuth2Flow.NotApprovedException as e:
        raise e
    except DropboxOAuth2Flow.ProviderException as e:
        raise e