from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

TYPES = (
    (1, "Fundacja"),
    (2, "Organizacja pozarządowa"),
    (3, "Zbiórka lokalna")
)

class Institution(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    type = models.IntegerField(choices=TYPES, default=1)
    categories = models.ManyToManyField(Category, blank=True)

    def cat_list(self):
        cat_list = ", ".join(cat.name for cat in self.categories.all())
        return cat_list



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

class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
