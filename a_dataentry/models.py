from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField(10)
    name = models.CharField(max_length=100)
    age = models.IntegerField(3)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    roll_no = models.IntegerField(10, null=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
     