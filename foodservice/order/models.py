from django.db import models
from django.contrib.auth.models import User
from employers.models import Employers

# Create your models here.


class Order(models.Model):
    tel = models.CharField(max_length=20)
    name = models.CharField(max_length=30, null=True)
    items = models.ManyToManyField('Items')
    status = models.ForeignKey('Status')
    user_accepted_order = models.FloatField(Employers, null=True)
    user_who_processed_order = models.ForeignKey(Employers, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_accepted = models.DateTimeField(null=True)
    date_delivered = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'order'

    def as_dict(self):
        dict_items = {
            'phone': self.tel,
            'name': self.name,
            'items': [i.as_dict() for i in self.items.all()],
            'number': self.order_number,
            'date_created': self.date_created,
            'date_accepted': self.date_accepted,
            'date_delivered': self.date_delivered,
            'user_accepted_order': self.user_accepted_order,
            'user_who_processed_order': self.user_accepted_order,
        }
        return dict_items


class Items(models.Model):
    item_name = models.CharField(max_length=30)
    item_description = models.TextField(max_length=1000)
    price = models.FloatField()
    image = models.ImageField()
    group = models.ForeignKey('FoodGroup', null=True)

    def __str__(self):
        return self.item_name

    class Meta:
        db_table = 'items'

    def as_dict(self):
        dict_items = {
            'name': self.item_name,
            'description': self.item_description,
            'price': self.price,
            'image': self.image
        }
        return dict_items


class FoodGroup(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'food_group'


class Status(models.Model):
    status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'statuses'

