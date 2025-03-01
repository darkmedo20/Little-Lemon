from django.db import models

# Create your models here.
'''class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()'''
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()
    
    
    
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=4, decimal_places=1)
    Inventory = models.IntegerField()
    def __str__(self):
        return f'{self.Title} : {str(self.Price)} {self.Inventory}'
    
class Drink(models.Model):
    name = models.CharField(max_length=255)
    temp = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.name} : {self.temp}'
    