from django.contrib import admin
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.order import Order


class customeradmin(admin.ModelAdmin):
       list_display=('first_name','last_name','phone','email','password')


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer,customeradmin)
admin.site.register(Order)