from django.db import models

# Create your models here.
class Cust_register(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=15)
    pincode = models.CharField(max_length=6)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)



class Profile_pictures(models.Model) :
    user = models.ForeignKey(Cust_register, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile/')