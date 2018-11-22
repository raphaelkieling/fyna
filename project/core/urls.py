from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('payment/new', views.payment_new, name='payment_new')
]