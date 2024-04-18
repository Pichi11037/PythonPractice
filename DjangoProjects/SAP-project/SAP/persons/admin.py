from django.contrib import admin
from persons.models import Person, Address, Country

# Register your models here.
admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Country)