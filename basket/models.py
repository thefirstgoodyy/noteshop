from django.db import models
from django.contrib.auth.models import User

from product.models import Good


class Basket(models.Model):
    owner = models.OneToOneField(User)


class BasketItem(models.Model):
    product = models.ForeignKey(Good)
    basket = models.ForeignKey(Basket)

    def __unicode__(self):
        return self.product.name
