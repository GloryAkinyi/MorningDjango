from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    date = models.DateField()
    department = models.CharField(max_length=200)
    doctor = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name
