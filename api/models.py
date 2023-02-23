from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Products(models.Model):
    name = models.CharField(unique=True, max_length=200)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField(null=True, upload_to='images')

    @property
    def avg_rating(self):
        rating = self.reviews_set.all().values_list("rating", flat=True)
        if rating:
            return sum(rating)/len(rating)
        else:
            return 0

    @property
    def no_rating(self):
        num = self.reviews_set.all().values_list("rating", flat=True)
        if num:
            return len(num)
        else:
            return 0

    def __str__(self):
        return self.name


class Carts(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    options=(
        ("order-placed","order-placed"),
        ("in-cart","in-cart"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=options,default="in-cart")


class Reviews(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment
   

class Orders(models.Model):
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("order-placed","order-placed"),
        ("despathed","depatched"),
        ("in-transit","in-transit"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=options,default="in-cart")
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=250)
    phone=models.CharField(max_length=20)
# orm
# orm for creating resource
# modelname.objects.create(field1=value1,field2=value2,.....)
# modelname.objects.create(name='anu',price=2300)

# Create your models here.
