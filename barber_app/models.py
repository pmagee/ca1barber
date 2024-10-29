from django.db import models
from django.urls import reverse # new

# Create your models here.
class BarberShop(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date_opened = models.DateField()

    def __str__(self):
        return self.name
    
    

class Barber(models.Model):
    name = models.CharField(max_length=200)
    num_customers = models.IntegerField()
    b_shop = models.ForeignKey(
        BarberShop,
        on_delete=models.CASCADE,
    )
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('b_detail', args=[str(self.id)])

class Customer(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    barber = models.ForeignKey(
        Barber,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
    


