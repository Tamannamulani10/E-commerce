from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import View
from store.models.customer import Customer


class Login(View):
    return_url = None
    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        return render(request,"login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        customer= Customer.get_customer_by_email(email)
        print(customer)
        customer = Customer.objects.get(email=email)

        if customer:

            if password == customer.password:
                request.session['customer_id'] = customer.id
                request.session['customer'] = customer.first_name
                if Login.return_url:
                   return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url=None
                    return redirect('homepage')

            else:
                print("Email or password not matched")
        return render(request, "login.html")
