from django.conf import settings
from django.db import models
from django.utils import timezone

# class User(models.Model):


class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    phone_num = models.TextField()
    address = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    recent_visit_date = models.DateTimeField(blank=True, null=True)

    def visit(self):
        self.recent_visit_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class OrderNumber(models.Model):
    order_number = models.CharField(max_length=8, primary_key=True)
    phone_num = models.ForeignKey('Customer', on_delete=models.CASCADE)
    num_clothes = models.DecimalField(max_digits=2, decimal_places=0)


class Order(models.Model):
    sub_order_number = models.CharField(max_length=10, primary_key=True)
    order_number = models.ForeignKey('OrderNumber', on_delete=models.CASCADE)
    clothes_code = models.ForeignKey('Clothe', on_delete=models.CASCADE)
    service_code = models.ForeignKey('Service', on_delete=models.CASCADE)
    status_code = models.ForeignKey('Status',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    stt_date = models.DateTimeField(default=timezone.now)
    est_date = models.DateTimeField(blank=True, null=True)
    fin_date = models.DateTimeField(blank=True, null=True)
    rtn_date = models.DateTimeField(blank=True, null=True)
    requiremnets = models.TextField(blank=True, null=True)
    

class Clothe(models.Model):
    clothes_code = models.CharField(primary_key=True, max_length=5)
    clothes = models.TextField()

class Service(models.Model):
    service_code = models.CharField(primary_key=True, max_length=5)
    service = models.TextField()

class Status(models.Model):
    status_code = models.CharField(primary_key=True, max_length=5)
    status = models.TextField()
