from django.db import models

# Create your models here.
class FormSubmission(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    materials = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name