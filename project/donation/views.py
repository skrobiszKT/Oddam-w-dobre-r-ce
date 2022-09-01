from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views import View

from donation.models import Donation, Institution


# Create your views here.

class LandingPageView(View):
    def get(self, request):
        donations = Donation.objects.all()
        quantity = 0
        for donation in donations:
            quantity = quantity + donation.quantity
        institutions = Institution.objects.all().count()
        ctx = {
            "quantity": quantity,
            "institutions": institutions
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
