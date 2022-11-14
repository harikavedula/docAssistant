from django.db import models

# Create your models here.
class Doctor(models.Model):
    dname=models.TextField(primary_key=True)
    dplace=models.TextField()
    specialisation=models.TextField()
    degrees=models.TextField()
    place=models.TextField()
    hospital=models.TextField()
    hospcity=models.TextField()
    phno=models.TextField()
    email=models.TextField()
    ambulance=models.TextField()

class Person(models.Model):
    id=models.TextField(primary_key=True)
    name=models.TextField()
    address=models.TextField()
    city=models.TextField()
    phno=models.TextField()
    email=models.TextField()
    


class Vitals(models.Model):
    vid=models.TextField(primary_key=True)
    id=models.TextField()
    date_time=models.TextField()
    Temprature=models.TextField()
    BloodPressure=models.TextField()
    Heartrate=models.TextField()


class Login(models.Model):
    email=models.TextField(primary_key=True)
    pswd=models.TextField()
    doc=models.TextField()

