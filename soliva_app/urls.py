from django.urls import path, re_path
from soliva_app.views import AppView
from soliva_app.forms import *

named_forms = [
    ('customer', CustomerForm),
    ('car', CarForm),
    ('address', AddressForm)
]

view_wizard = AppView.as_view(named_forms, url_name='view_step', done_step_name='finished')

urlpatterns = [
    re_path(r'^view/(?P<step>.+)/$', view_wizard, name='view_step'),
    path('', view_wizard, name='view'),
]