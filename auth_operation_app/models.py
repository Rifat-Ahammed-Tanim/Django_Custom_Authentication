from django.db import models
from django.contrib.auth.models import AbstractUser 

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    present_address = models.TextField()
    profile_image = models.ImageField(upload_to='Media/profile_images/')