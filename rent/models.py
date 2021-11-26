from django.db import models


# Create your models here.
class Customer(models.Model):
    first = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.PositiveIntegerField
    number = models.PositiveIntegerField
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)


class VehicleType(models.Model):
    name = models.CharField(max_length=200)


class VehicleSize(models.Model):
    name = models.CharField(max_length=200)


class Vehicle(models.Model):
    date_created = models.DateField(null=True)
    real_cost = models.PositiveIntegerField
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)


class Rental(models.Model):
    rental_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class Rental_rate(models.Model):
    daily_rate = models.PositiveIntegerField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
