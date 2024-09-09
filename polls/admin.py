from django.contrib import admin
from .models import Client
from .models import ClientAnimal
from .models import TypeAnimal
from .models import Booking



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['time' ,'date' , 'client']
    list_filter = ['time', 'date' , 'client']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name' ,'surname' , 'number']


@admin.register(ClientAnimal)
class ClientAnimalAdmin(admin.ModelAdmin):
    list_display = ['age' ,'client' , 'typeanimal']

admin.site.register(TypeAnimal)






