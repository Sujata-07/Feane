from django.contrib import admin
from .models import Contact
from .models import Booking
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    clist=['name','email','message']
admin.site.register(Contact,ContactAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'persons', 'booking_date']
    admin.site.register(Booking)
