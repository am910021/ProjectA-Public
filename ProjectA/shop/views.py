from main.views import BaseView


class CShop(BaseView):
    def get(self, request, *args, **kwargs):
        return BaseView.get(self, request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(CShop, self).post(request, *args, **kwargs)