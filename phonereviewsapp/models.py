from django.db import models
from django.contrib.auth.models import User

from datetime import date


class Phone(models.Model):

    name = models.TextField()
    phone_model = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    screen = models.TextField(default="")
    processor = models.TextField(blank=True, null=True)
    RAM = models.TextField(blank=True, null=True)
    memory = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="phonereviewsapp", blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.PROTECT)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name


class Store(models.Model):

    name = models.TextField()
    street = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    city = models.TextField(default="")
    zipCode = models.TextField(blank=True, null=True)
    stateOrProvince = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="phonereviewsapp", blank=True, null=True)
    phone = models.ForeignKey(Phone, null=True, related_name='stores', on_delete=models.PROTECT)
    user = models.ForeignKey(User, default=1, on_delete=models.PROTECT)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True, default=" ")
    user = models.ForeignKey(User, default=1, on_delete=models.PROTECT)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True


class PhoneReview(Review):
    phone = models.ForeignKey(Phone, on_delete=models.PROTECT)
