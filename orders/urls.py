from django.urls import path, re_path
from . import views

app_name = 'orders'
urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    re_path(r'^admin/order/<(?P<order_id>\d+)/$', views.admin_order_detail, name='admin_order_detail'),
]