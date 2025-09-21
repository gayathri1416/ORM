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



# Create your models here.
