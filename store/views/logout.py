from django.shortcuts import render,redirect
from django.views import View
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password




class Logout(View):
    temp = True

    def get(self, request):
        return render(request, "logout.html")


    def post(self, request):
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        request.session.clear()
        return redirect('homepage')

        self.temp = True
        if not Email or not Password:
            return render(request, "logout.html", {'error': 'Email and Password are required', 'temp': self.temp})

        try:
            customer = Customer.objects.get(Email=Email)
        except Customer.DoesNotExist:
            return render(request, "logout.html", {'error': 'Customer does not exist', 'temp': self.temp})

        if check_password(Password, customer.Password):
            customer.delete()
            return redirect('homepage')  # Redirect to the main page after successful logout
        else:
            return render(request, "logout.html", {'error': 'Invalid password', 'temp': self.temp})

        return render(request, "logout.html", {'temp': self.temp})





