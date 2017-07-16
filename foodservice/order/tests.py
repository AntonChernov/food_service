from django.test import TestCase
from order.models import *
from employers.models import *
# Create your tests here.


class NewOrderSetUp(TestCase):

    def setUp(self):
        user_accept_operator = User.objects.create(
            username='accept_operator',
            password='qwerty12345'
        )
        user_processed_order = User.objects.create(
            username='deliveryman',
            password='qwerty12345'
        )
        position_accept_operator = Positions.objects.create(
            position_name='accept_operator',
        )
        position_deliveryman = Positions.objects.create(
            position_name='deliveryman',
        )

        Employers.objects.create(
            user=user_accept_operator,
            name='Сергій Василійович Сірко',
            phone='+380509874987',
            position=position_accept_operator,
            online=True,
            dismissed=False,
        )
        Employers.objects.create(
            user=user_processed_order,
            name='Василина Тарасівна Ріжко',
            phone='+380504789885',
            position=position_deliveryman,
            online=True,
            dismissed=False,
        )