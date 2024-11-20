from django.db import models
from Accounts.models import Cust_register
 # Create your models here.

class Pets(models.Model) :
    name = models.CharField()
    age = models.IntegerField()
    breed = models.CharField()
    gender = models.CharField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='pets/')
    quantity = models.IntegerField(default=1)


class Cart(models.Model) :
    user = models.ForeignKey(Cust_register, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pets, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(default=0)
    grand_total = models.IntegerField(default=0)



class Payments(models.Model):
    user=models.ForeignKey(Cust_register,on_delete=models.CASCADE)
    pet=models.ForeignKey(Cart,on_delete=models.CASCADE)
    amount=models.FloatField()
    payment_id = models.CharField()



class Delivery_details(models.Model):
    user=models.ForeignKey(Cust_register,on_delete=models.CASCADE)
    pet=models.ForeignKey(Cart,on_delete=models.CASCADE)
    amount=models.FloatField()
    address = models.CharField()
    user_token = models.IntegerField()
    delivery_token = models.IntegerField()
    delivery_status = models.CharField(max_length=20, default='Pending')
    
