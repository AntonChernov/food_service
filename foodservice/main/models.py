from django.db import models

# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_description = models.TextField(max_length=1500)
    company_address = models.TextField(max_length=500)
    company_map_lat = models.FloatField(null=True)
    company_map_lng = models.FloatField(null=True)

    class Meta:
        db_table = 'company'

    def __str__(self):
        return self.company_name

    def as_dict(self):
        items = {
            'name': self.company_name,
            'description': self.company_description,
            'address': self.company_address,
            'lat': self.company_map_lat,
            'lng': self.company_map_lng,
        }
        return items
