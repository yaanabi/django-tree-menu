from django.test import RequestFactory, TestCase
from django.template import Template, Context
from django.urls import reverse


# Create your tests here.
class QueriesMadeTest(TestCase):

    def test_queries_made(self):
        with self.assertNumQueries(1):
            self.client.get('/')
