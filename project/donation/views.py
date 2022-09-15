from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from donation.models import Donation, Institution, Category


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

class AddDonationView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        ctx = {
            "categories": categories,
            "institutions": institutions
        }
        return render(request, "form.html", ctx)
    def post(self, request):
        categories_id_list = request.POST.getlist('categories')
        categories = []
        for cat_id in categories_id_list:
            category = get_object_or_404(Category, id=cat_id)
            categories.append(category)

        bags = request.POST.get('bags')
        institution_id = request.POST.get('organization')
        institution = get_object_or_404(Institution, id=institution_id)
        address = request.POST.get('address')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        date = request.POST.get('data')
        time = request.POST.get('time')
        comment = request.POST.get('more_info')

        donation = Donation.objects.create(quantity=bags, institution=institution,
                                           address=address,
                                           phone_number=phone,
                                           city=city,
                                           zip_code=postcode,
                                           pick_up_date=date,
                                           pick_up_time=time,
                                           pick_up_comment=comment,
                                           user=request.user
                                           )

        for category in categories:
            donation.categories.add(category)

        return render(request, "form-confirmation.html", {})



class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        username = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
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

class LogoutView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        logout(request)
        return redirect("index")

class ProfileView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        return render(request, "profile.html", {})
