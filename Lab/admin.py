from django.contrib import admin,auth

from . import models


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    list_filter = ('name', 'phone')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('customer', 'plane', 'price')
    list_filter = ('customer', 'plane', 'price')


class PlaneAdmin(admin.ModelAdmin):
    list_display = ('city_from', 'city_to', 'departure_date', 'departure_time',
                    'landing_date', 'landing_time')
    list_filter = ('city_from', 'city_to', 'departure_date', 'departure_time',
                    'landing_date', 'landing_time')


admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Ticket, TicketAdmin)
admin.site.register(models.Plane, PlaneAdmin)
