from django.db import models

# Create your models here.


class Good(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    picture = models.ImageField(upload_to='product_pictures')
    label = models.ForeignKey('Label')
    size = models.FloatField()
    hdd_mass = models.PositiveIntegerField()
    ram = models.PositiveIntegerField()
    processor = models.CharField(max_length=20)
    dvd = models.BooleanField()
    usb = models.PositiveIntegerField()
    videocard = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()

    def __unicode__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='label_pictures')

    def __unicode__(self):
        return self.name
