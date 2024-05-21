from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=30,null=False,blank=False)
    roll=models.IntegerField(null=False,blank=False)
    city=models.CharField(max_length=30,null=False,blank=False)

    def __str__(self):
        return self.name