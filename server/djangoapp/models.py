# Uncomment the following imports before adding the Model code
from django.db import models

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    CAR_TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('wagon', 'Wagon'),
        ('hatchback', 'Hatchback'),
        ('coupe', 'Coupe'),
        ('convertible', 'Convertible'),
        ('pickup', 'Pickup Truck'),
        ('van', 'Van'),
        ('crossover', 'Crossover'),
    ]
    FUEL_TYPE_CHOICES = [
        ('gasoline', 'Gasoline'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),
        ('plug_in_hybrid', 'Plug-in Hybrid'),
    ]
    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ]
    name = models.CharField(max_length=100)
    car_make = models.ForeignKey(
        'CarMake', 
        on_delete=models.CASCADE,
        related_name='car_models'
    )
    dealer_id = models.IntegerField(
        null=True,
        blank=True,
        help_text="Dealer ID from Cloudant database"
    )
    type = models.CharField(
        max_length=20,
        choices=CAR_TYPE_CHOICES,
        default='sedan'
    )
    year = models.IntegerField()
    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_TYPE_CHOICES,
        default='electric'
    )
    transmission = models.CharField(
        max_length=20,
        choices=TRANSMISSION_CHOICES,
        default='automatic'
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
