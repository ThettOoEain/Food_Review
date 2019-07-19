from django.db import models

# Create your models here.

class Restaurant(models.Model):
    
    name = models.CharField(max_length=200 )
    address = models.CharField(max_length=500)

    def __str__(self):
        return '{}'.format(self.name)

class Restaurant_Review(models.Model):
    
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    review = models.CharField(max_length=500)
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    service_charges = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '{}/{}/{}/{}'.format(self.review, self.rating, self.restaurant, self.price)

class Review_Detail(models.Model):
    
    restaurant_review = models.ForeignKey('Restaurant_Review', on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return '{}/{}'.format(self.comment,self.restaurant_review)