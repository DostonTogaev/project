from django.db import models


# Create your models here.

class Product(models.Model):
    class RatingChoice(models.IntegerChoices):
        Zero = 0
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    rating = models.IntegerField(choices=RatingChoice.choices, default=RatingChoice.Zero.value)
    amount = models.IntegerField(default=1)
    discount = models.IntegerField()
    attribute = models.ManyToManyField('Attribute', blank=True,  related_name='attributes')
    # attribute_value = models.ManyToManyField('AttributeValue', blank=True, null=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('app.Product', on_delete=models.CASCADE, related_name='images')


class Attribute(models.Model):
    attribute_name = models.CharField(max_length=100)

    def __str__(self):
        return self.attribute_name

class Specific(models.Model):
    specific_name = models.CharField(max_length=20)

    def __str__(self):
        return self.specific_name

class Specific_value(models.Model):
    specific = models.ForeignKey('Specific', on_delete=models.CASCADE, related_name='values')
    specific_value = models.CharField(max_length=20)

    def __str__(self):
        return self.specific_value

class Customers(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    Phone = models.IntegerField()
    Billing_address = models.CharField(max_length=100)
    Joined = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.full_name