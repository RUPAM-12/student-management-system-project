from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    course = models.CharField(max_length=150)
    address = models.TextField()
    
    # date_ok = models.DateField(auto_now_add=True,null=True,blank=True)
    # # time_ok = models.TimeField()
    # salary = models.DecimalField(decimal_places=2, max_digits=10,null=True,blank=True)
    