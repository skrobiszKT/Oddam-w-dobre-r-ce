from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views import View

from donation.models import Donation, Institution, TYPES


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
            "types": TYPES
        }
        return render(request, "index.html", ctx)

class AddDonationView(View):
    def get(self, request):
        return render(request, "form.html", {})

class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

class RegisterView(View):
    def get(self, request):
        return render(request, "register.html", {})
