import datetime

from django.db import models
from store.models.product import Product
from store.models.customer import Customer


class Order(models.Model):
      product= models.ForeignKey(Product, on_delete=models.CASCADE)
      customer =models.ForeignKey(Customer, on_delete=models.CASCADE)
      quantity= models.IntegerField(default=1)
      price= models.IntegerField()
      address=models.CharField(max_length=250 , default='',blank='')
      phone=models.CharField(max_length=10 ,default='',blank='')
      date= models.DateField(default=datetime.datetime.today)
      status=models.BooleanField(default=False)


      def placeorder(self):
         self.save()



      @staticmethod
      def get_orders_by_customer(customer_id):
           return Order \
               .objects \
               .filter(customer=customer_id)\
               .order_by('-date')