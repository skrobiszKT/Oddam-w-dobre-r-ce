from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
# Create your views here.

class LandingPageView(View):
    def get(self, request):
        return render(request, "index.html", {})

class AddDonationView(View):
    def get(self, request):
        return render(request, "form.html", {})

class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

class RegisterView(View):
    def get(self, request):
        return render(request, "register.html", {})
