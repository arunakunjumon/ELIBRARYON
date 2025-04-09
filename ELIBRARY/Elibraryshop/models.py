from django.db import models

# Create your models here.

#user register
class user_reg(models.Model):
    name = models.CharField(max_length=100)
    phone= models.IntegerField()
    email= models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='books/', default='default.jpg')

    def __str__(self):
        return self.title


    