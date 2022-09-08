from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from donation.models import Donation, Institution


# Create your views here.

class LandingPageView(View):
    def get(self, request):
        donations = Donation.objects.all()
        quantity = 0
        for donation in donations:
            quantity = quantity + donation.quantity
        institutions = Institution.objects.all().count()
        institutions_type_1 = Institution.objects.filter(type=1)
        institutions_type_2 = Institution.objects.filter(type=2)
        institutions_type_3 = Institution.objects.filter(type=3)
        ctx = {
            "quantity": quantity,
            "institutions": institutions,
            "type1": institutions_type_1,
            "type2": institutions_type_2,
            "type3": institutions_type_3,
        }
        return render(request, "index.html", ctx)

class AddDonationView(View):
    def get(self, request):
        return render(request, "form.html", {})

class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        username = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return redirect("register")

class RegisterView(View):
    def get(self, request):
        return render(request, "register.html", {})

    def post(self, request):
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        new_user = User.objects.create_user(
            username=email, email=email, password=password, first_name=name, last_name=surname
        )

        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("index")
