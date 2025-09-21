# Ex02 Django ORM Web Application
# Date:
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
``` 
admin.py 

from django.contrib import admin
from .models import CarInventory,CarInventoryAdmin
admin.site.register(CarInventory,CarInventoryAdmin)

models.py
 
from django.db import models
from django.contrib import admin 

class CarInventory(models.Model):
    car_selling_no=models.IntegerField(primary_key=True)
    brand=models.CharField(max_length=20)
    fuel_type=models.CharField(max_length=10)
    price=models.IntegerField()
    color=models.CharField(max_length=10)
    warranty=models.DateField()

class CarInventoryAdmin(admin.ModelAdmin):
    list_display=('car_selling_no','brand','fuel_type','price','color','warranty')
```


## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
# OUTPUT
![alt text](<Screenshot 2025-09-21 181919.png>)



# RESULT
Thus the program for creating a database using ORM hass been executed successfully
