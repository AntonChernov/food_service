from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employers(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=300, null=True)
    position = models.ForeignKey('Positions')
    dismissed = models.BooleanField(default=False)
    online = models.BooleanField(default=False)

    class Meta:
        db_table = 'employers'

    def as_dict(self):
        items = {
            'user': self.user.username,
            'user_id': self.user.id,
            'employer_id': self.id,
            'name': self.name,
            'phone': self.phone,
            'location': self.location,
            'dismissed': self.dismissed,
        }
        return items

    def __str__(self):
        return self.name


class SiteAdmin(models.Model):
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


class Positions(models.Model):
    position_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'positions'

    def __str__(self):
        return self.position_name
