from django.test import TestCase
from .models import Person

# Create your tests here.

class  PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.perso=Person.objects.create(
            first_name="sandeepa",
            last_name="T N"
        )


    def test_fields(self):
        self.assertIsInstance(self.perso.first_name,int)
        self.assertIsInstance(self.perso.last_name,str)