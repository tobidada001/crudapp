from django.db import models



class Employee (models.Model):
    firstname = models.CharField(max_length= 50)
    lastname = models.CharField(max_length= 50)
    email = models.CharField(max_length= 50)
    password = models.CharField(max_length= 50)

    def __str__(self):
        return  self.firstname + ' '+ self.lastname


# Create your models here.
