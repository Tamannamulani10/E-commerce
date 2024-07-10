from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.views import View
from store.models.customer import Customer
from store.models.product import Product
from store.models.order import Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class Orderview(View):
    def get(self,request):
        customer=request.session.get('customer_id')
        orders =Order.get_orders_by_customer(customer)
        print(orders)
        return render(request,"orders.html",{'orders':orders})