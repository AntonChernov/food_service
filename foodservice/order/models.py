from django.db import models

# Create your models here.


class Order(models.Model):
    tel = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    new = models.BooleanField(default=True)
    order_number = models.BigIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'order'

    def as_dict(self):
        dict_items = {
            'phone': self.tel,
            'name': self.name,
            'items': self.items,
            'number': self.order_number
        }
        return dict_items


class Items(models.Model):
    item_name = models.CharField(max_length=30)
    item_description = models.TextField(max_length=1000)
    price = models.FloatField()
    image = models.ImageField()
    group = models.ForeignKey(FoodGroup, null=True)

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
