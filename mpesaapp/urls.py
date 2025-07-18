from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pay/',views.lipa_na_mpesa_online,name='pay'),
    path('callback/',views.callback,name='callback'),
    path('paymentinfo/',views.payment_info,name='paymentinfo')
]