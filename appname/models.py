from django.db import models

# # Create your models here.
# class Data(models.Model):

#     name = models.CharField(max_length=60)
#     body = models.CharField(max_length=200)

#     def __str__(self):

#         return self.name

class Point(models.Model):
    vehicle_name = models.CharField(max_length=10)

    def __str__(self):
        return self.vehicle_name
