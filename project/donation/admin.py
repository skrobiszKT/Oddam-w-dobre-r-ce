from django.contrib import admin
from donation.models import Donation, Institution, Category

# Register your models here.
admin.site.register(Donation)
admin.site.register(Category)
admin.site.register(Institution)