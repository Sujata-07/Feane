from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    def _str_(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):


    nm = models.CharField(max_length=100)  # Name
    ph = models.CharField(max_length=15)   # Phone number
    em = models.EmailField()               # Email
    gu = models.IntegerField()             # Number of guests
    da = models.DateField()                # Date

    def __str__(self):
        return f"{self.nm} - {self.ph} - {self.gu} guests"
