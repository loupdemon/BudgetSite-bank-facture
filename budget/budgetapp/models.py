from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class User(User):
    #user_id = models.BigAutoField(primary_key=True)
    #username = models.CharField(max_length=50)
    #https://stackoverflow.com/questions/17523263/how-to-create-password-field-in-model-django
    #def __str__(self):
        #return self.username
    pass

class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=0 , on_delete=models.CASCADE)
    category_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=19,decimal_places=2)
    def __str__(self):
        return self.category_name

class Ledger(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #primary_key=True might cause problems
    transaction_id = models.BigAutoField(primary_key=True)
    transaction_time = models.DateTimeField (auto_now=True) #should it be auto_now?
    amount = models.DecimalField(max_digits=19,decimal_places=2)
    description = models.CharField(max_length=50)