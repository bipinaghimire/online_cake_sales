from django.db import models

# Create your models here.

class Customer(models.Model):
    id =models.AutoField(auto_created=True,primary_key=True)
    fullname = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default="")
    image = models.FileField(upload_to="static/images/customer", default="default.jpg") #kata upload garni vanera 

    class Meta:
        db_table = "customer"
