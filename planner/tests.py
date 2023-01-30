from datetime import datetime
import json

from django.test import TestCase

from planner.models import Record


class PlannerAPITest(TestCase):
    """test planners API """

    base_url = '/api/planner/records/{}/'

    def test_get_returns_json_200(self):
        """test: returns json and status 200"""
        record = Record.objects.create(title="Test record", content="test content")
        response = self.client.get(self.base_url.format(record.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_get_returns_record_correct(self):
        """test: returns correct json record"""
        dt = datetime.strptime("21/01/23 16:30", "%d/%m/%y %H:%M")
        record = Record.objects.create(title="Test record", content="test content", сreated_at=dt)
        good_result = {
            'id': record.id,
            'title': 'Test record',
            'content': 'test content',
            'created_at': dt
        }
        response = self.client.get(self.base_url.format(record.id))
        print(response.content)
        self.assertEqual(json.loads(response.content.decode('utf8')), good_result)
