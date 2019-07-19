from django.contrib import admin

from .models import Restaurant, Restaurant_Review,Review_Detail
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Restaurant_Review)
admin.site.register(Review_Detail)
