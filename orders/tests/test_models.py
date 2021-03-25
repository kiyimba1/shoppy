from django.test import TestCase

from orders.models import Order, OrderItem

class OrderTestCase(TestCase):
    @classmethod
    def setUpTestData(self) -> None:
        Order.objects.create(first_name='first', last_name='last', email='email@test.com', address='address', postal_code='26565', city='city')