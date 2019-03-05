from django.db import models


class FishSauce(models.Model):
    name_product = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    produce_date = models.DateField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    quanity = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', null=False, blank=False)
    type_product = models.IntegerField(default=1)
    volume = models.FloatField(default=0, blank=True, null=True)
    protein = models.FloatField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'fishsauce'


class Company(models.Model):
    name_company = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=400)
    class Meta:
        db_table = "company"


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = "member"