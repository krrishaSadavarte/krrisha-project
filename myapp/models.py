from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.first_name
    

class blog(models.Model):
    cate=[
         ('Vegetarian','Vegetarian'),
         ('non-veg','non-veg'),
         ('dessert and drinks','dessert and drinks')
    ]
    recipe_name = models.CharField(max_length=150)
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    file = models.FileField(upload_to='blog_images')
    categories = models.CharField(max_length=150,choices=cate)
    def __str__(self) -> str:
           return self.username
  

class Payment(models.Model):
    pay_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    pay_to = models.ForeignKey(blog, on_delete=models.CASCADE)
    amount = models.IntegerField()
    time = models.DateTimeField(auto_now=True)
    