from django.db import models
from datetime import datetime

#no foreignkey connnections to user and listings
class Contact(models.Model):
    listing=models.CharField(max_length=200)
    listing_id=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    contact_date=models.DateTimeField(default=datetime.now, blank=True)
    user_id=models.IntegerField(blank=True) #it is possible for someone not logged in to make an inquiry
    def __str__(self):
        return self.name