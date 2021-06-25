from django.contrib import admin
from .models import Profile, Product, ProductCategory, BabyAge
# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(BabyAge)