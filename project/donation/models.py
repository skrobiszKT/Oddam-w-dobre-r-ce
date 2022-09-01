from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

TYPES = (
    (1, "fundacja"),
    (2, "organizacja porządkowa"),
    (3, "zbiórka lokalna")
)

class Institution(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    type = models.IntegerField(choices=TYPES, default=1)
    categories = models.ManyToManyField(Category, blank=True)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE,
                                             null=True)
    address = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField(null=True)
    pick_up_time = models.DateTimeField(null=True)
    pick_up_comment = models.TextField(null=True)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
