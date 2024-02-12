from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    price=models.IntegerField()
    category=models.CharField(max_length=20)
    stock=models.IntegerField(default=100)
    qty=models.CharField(max_length=40,default='kilogram')
    image=models.ImageField(upload_to='static/image/')

    def __str__(self):
        return self.name

class Orders(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    zip_code = models.CharField(max_length=10)
    cart_data = models.JSONField()
    payment_method = models.CharField(max_length=20, choices=[
        ('credit', 'Credit Card'),
        ('cash', 'Cash'),
        ('upi', 'UPI Payments'),
    ], default='cash')

    def __str__(self):
        return f"Order #{self.id} - {self.first_name} {self.last_name}"

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
