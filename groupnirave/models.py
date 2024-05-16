from django.db import models

# Create your models here.

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True) #gender_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    gender = models.CharField(max_length=55) #gender VARCHAR(55) NOT NULL
    created_at = models.DateTimeField(auto_now_add=True) # created_at TIMESTAMP DEFAULT CURRENT TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) # updated_at TIMESTAMP DEFAULT CURRENT_TIME UPDATE CURRENT_TIMESTAMP

    class Meta:
        db_table = 'genders'

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55)
    age = models.IntegerField()
    birthday = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
