from django.db import models


class Customer(models.Model):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email=models.EmailField(unique=True)
    password = models.CharField(max_length=50)



    @staticmethod
    def get_customer_by_email(email):
        try:
          return Customer.objects.get(email=email)
        except:
            return False







