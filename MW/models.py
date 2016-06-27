from __future__ import unicode_literals

from django.db import models



# Create your models here.

class Site(models.Model):
    site_name = models.CharField(max_length=200)
    def __str__(self):
        return self.site_name

class Value(models.Model):
    value_A = models.FloatField()
    value_B = models.FloatField()
    pub_date = models.DateField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.value_A.__str__() + " | " + self.value_B.__str__()