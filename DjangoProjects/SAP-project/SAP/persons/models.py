from django.db import models

# Create your models here.

class Country(models.Model):
    name  = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=8)

    def __str__(self) -> str:
        return f'Country {self.id}: {self.name} {self.abbreviation}'
    

class Address(models.Model):
    street = models.CharField(max_length=255)
    streetNo = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null = True)

    def __str__(self) -> str:
        return f'Address {self.id}: {self.street} {self.streetNo} {self.country}'

class Person(models.Model):
    
    name = models.CharField( max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'Person {self.id}: {self.name} {self.lastName} {self.email}'