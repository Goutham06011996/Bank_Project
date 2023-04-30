from django.db import models
from django.db import models
from django.contrib.auth.models import User

class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20)
    debit_card = models.BooleanField(default=0)
    credit_card = models.BooleanField(default=0)
    cheque_book = models.BooleanField(default=0)
    user_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name


