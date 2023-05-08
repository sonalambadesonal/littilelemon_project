from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    guest_number = models.IntegerField()
    table_directions = [('Middle', 'Middle'), ('Center', 'Center'), ('Corner', 'Corner'), ('VIP', 'VIP')]
    table_choise = models.CharField(max_length=50, choices=table_directions)

    def __str__(self):
        return self.first_name
    
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    menu_item_description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
    