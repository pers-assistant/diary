from django.test import TestCase

from planner.models import Record

# Create your tests here.

class PlannerAPITest(TestCase):
    """test planners API """

    base_url = '/api/planner/records/{}'

    def test_get_returns_json_200(self):
        """test: returns json and status 200"""
        record = Record.objects.create()
        response = self.client.get(self.base_url.format(record.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')