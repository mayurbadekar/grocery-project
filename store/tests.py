from django.test import TestCase
from .models import Feedback

# Create your tests here.
class ShippingTest(TestCase):
    def setUp(self) -> None:
        print('setUp method ....')
        Feedback.objects.create(name='dj',email='ha@gmail.com',mobile_no='9867037823',message='EK no')

    def test_method(self):
        print('Testing starts...')
        qs=Feedback.objects.all()
        self.assertEquals(qs.count(),1)
        f1=Feedback.objects.get(name='dj')




