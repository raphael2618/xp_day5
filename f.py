from faker import Faker
import os
import django
import random
fake= Faker()

django.setup()

from rent.models import *
# VehicleType.objects.create(name='Bike')
# VehicleType.objects.create(name='E-Bike')
# VehicleType.objects.create(name='Scooter')
# VehicleType.objects.create(name='Jet-Pack')
#
#
# VehicleSize.objects.create(name='Small')
# VehicleSize.objects.create(name='Medium')
# VehicleSize.objects.create(name='Large')
#
# for type in VehicleType.objects.filter(name = 'Bike'):
#         rate = 5
#         for size in VehicleSize.objects.all():
#             RentalRate.objects.create(daily_rate= rate, vehicle_type=VehicleType.objects.get(name= type.name),vehicle_size=VehicleSize.objects.get(name= size.name))
#             rate +=2
#
# for type in VehicleType.objects.filter(name='E-Bike'):
#         rate = 10
#         for size in VehicleSize.objects.all():
#             RentalRate.objects.create(daily_rate= rate, vehicle_type=VehicleType.objects.get(name= type.name),vehicle_size=VehicleSize.objects.get(name= size.name))
#             rate +=4
#
# for type in VehicleType.objects.filter(name='Scooter'):
#         rate = 15
#         for size in VehicleSize.objects.all():
#             RentalRate.objects.create(daily_rate= rate, vehicle_type=VehicleType.objects.get(name= type.name),vehicle_size=VehicleSize.objects.get(name= size.name))
#             rate +=8
#
# for type in VehicleType.objects.filter(name='Jet-Pack'):
#         rate = 200
#         for size in VehicleSize.objects.all():
#             RentalRate.objects.create(daily_rate= rate, vehicle_type=VehicleType.objects.get(name= type.name),vehicle_size=VehicleSize.objects.get(name= size.name))
#             rate +=100
#
#
#
#
# print(RentalRate.objects.all())

# for i in range(10):
#     Customer.objects.create(first_name=fake.first_name(),last_name=fake.last_name() ,email=fake.email() ,phone_number= fake.phone_number(),address=fake.address() ,city=fake.city() ,country=fake.country())


# for type in VehicleType.objects.filter(name='Bike'):
#     cost= 100
#     for size in VehicleSize.objects.all():
#         Vehicle.objects.create(vehicle_type=type,date_created= fake.date() ,real_cost= cost,size=size)
#         cost += 50
# for type in VehicleType.objects.filter(name='E-Bike'):
#     cost= 150
#     for size in VehicleSize.objects.all():
#         Vehicle.objects.create(vehicle_type=type,date_created= fake.date() ,real_cost= cost,size=size)
#         cost += 50
#
# for type in VehicleType.objects.filter(name='Scooter'):
#     cost= 75
#     for size in VehicleSize.objects.all():
#         Vehicle.objects.create(vehicle_type=type,date_created= fake.date() ,real_cost= cost,size=size)
#         cost += 25
#
# for type in VehicleType.objects.filter(name='Jet-Pack'):
#     cost= 1000
#     for size in VehicleSize.objects.all():
#         Vehicle.objects.create(vehicle_type=type,date_created= fake.date() ,real_cost= cost,size=size)
#         cost += 200