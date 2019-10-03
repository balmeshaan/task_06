from django.db import models
from django.urls import reverse

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def get_absolute_url(self):
    	return reverse('restaurant-detail', kwargs={'restaurant_id':self.id})
