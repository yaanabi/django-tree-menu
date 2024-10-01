from django.test import TestCase


# Create your tests here.
class QueriesMadeTest(TestCase):

    def test_queries_made(self):
        with self.assertNumQueries(1):
            self.client.get('/')
