from django.db import models

class Employee (models.Model):

    name = models.CharField(max_length=200)

    department = models.CharField(max_length=200)

    salary = models.PositiveIntegerField()

    location = models.CharField(max_length=200)

    age = models.IntegerField()

    experience = models.IntegerField()

    
    def __str__(self):

        return self.name


    
