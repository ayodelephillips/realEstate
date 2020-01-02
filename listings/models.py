from django.db import models
from datetime import datetime
from realtors.models import Realtor
# Create your models here.
class Listing(models.Model):
    realtor=models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200) #most times title and address are same
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=20)
    description=models.TextField(blank= True)
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.DecimalField(max_digits=2, decimal_places=1) #incase we have 2 and a half bathrooms
    garage=models.IntegerField(default=0)
    sqft=models.IntegerField()
    lot_size=models.DecimalField(max_digits=5,decimal_places=1) #its gonna be measured in acres
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/') #
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) #
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) #
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) #
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) #
    photo_5=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) #
    photo_6=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) #
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now,blank=True)

    #allows the title to be returned in admin page, and not the object
    def __str__(self):
        return (self.title)
