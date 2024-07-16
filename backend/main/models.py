from django.db import models
from django.contrib.auth.models import AbstractUser

# User --------------------------------------------------
class MainUser(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=30, default='')
    licence = models.CharField(max_length=10)
    email = models.EmailField()  

    def __str__(self):
        return self.username
    
# Storage ------------------------------------
class Storage(models.Model):
    storage_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=80)
    user_id = models.ForeignKey(MainUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "storage"

    def __str__(self):
        return self.name

# Medication --------------------------------------------------------
class Medication(models.Model):
    medication_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    dose = models.CharField(max_length=50)
    amount = models.CharField(max_length=100)
    user_id = models.ForeignKey(MainUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "Medication"

# Employee -------------------------------------------------------
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255) 
    licence_tem = models.CharField(max_length=100)
    expirate = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    user_id = models.ForeignKey('MainUser', on_delete=models.CASCADE)

    class Meta:
        db_table = "employee"