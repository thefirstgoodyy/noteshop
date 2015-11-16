from django.contrib import admin

# Register your models here.
from product.models import Good, Label

admin.site.register(Good)
admin.site.register(Label)
