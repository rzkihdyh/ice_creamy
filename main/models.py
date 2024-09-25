import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField() 
    description = models.TextField()
    quantity = models.IntegerField(default=0)  
    stock = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE)