from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Emploue(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=120)
    phone = models.IntegerField(max_length=20)
    location = models.CharField(max_length=300)
    login_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'emplouers'

    def as_dict(self):
        items = {
            'user': self.user,
            'name': self.name,
            'phone': self.phone,
            'location': self.location,
            'login_name': self.login_name
        }
        return items

    def __str__(self):
        return self.name


class Admin(models.Model):
    user = models.ForeignKey(User)
    phone = models.IntegerField(max_length=20)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'admin'

    def as_dict(self):
        items = {
            'user': self.user,
            'phone': self.phone,
            'name': self.name
        }
        return items

    def __str__(self):
        return self.name
