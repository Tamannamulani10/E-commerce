from django.shortcuts import render,redirect
from django.views import View
from store.models.customer import Customer

class Signup(View):
    def get(self,request):
        return render(request,"signup.html")

    def post(self,request):
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        password=request.POST.get("password")
        customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
        print(customer)
        customer.save()
        request.session['customer'] = customer.first_name
        return redirect('homepage')



