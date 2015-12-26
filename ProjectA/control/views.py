from main.views import BaseView, admin_required

class AdminRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return admin_required(super(AdminRequiredMixin, cls).as_view())
    
class AdminView(AdminRequiredMixin,BaseView):
    def __init__(self, *args, **kwargs):
        super(AdminView, self).__init__(*args, **kwargs)


class CAdminIndex(AdminView):
    template_name = 'control/index.html'
    page_title = '管理者'
    
    def get(self, request, *args, **kwargs):
        return AdminView.get(self, request, *args, **kwargs)