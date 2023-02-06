from datetime import datetime
import json

from django.test import TestCase

from planner.models import Record


class PlannerAPITest(TestCase):
    """test planners API """

    base_url = '/api/planner/records/'

    record_data = {
        'title': 'Test record',
        'content': 'test content',
    }

    def test_get_returns_json_200(self):
        """test: returns json and status 200"""
        record = Record.objects.create(title="Test record", content="test content")
        response = self.client.get(f"{self.base_url}{record.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_get_returns_record_correct(self):
        """test: returns correct json record"""
        cdate = datetime.strptime("2020-11-06 16:30", "%Y-%m-%d %H:%M")
        record = Record.objects.create(title="Test record", content="test content", created_at=cdate)
        good_result = {
            'id': record.id,
            'title': 'Test record',
            'content': 'test content',
            'created_at': cdate
        }
        response = self.client.get(f"{self.base_url}{record.id}/")
        self.assertEqual(json.loads(response.content.decode('utf8'))['title'], good_result['title'])

    def test_post_new_record(self):
        """test: create new record"""
        record_dict = {
            'title': 'Test record',
            'content': 'test content',
        }
        response = self.client.post(self.base_url, record_dict)
        self.assertEqual(response.status_code, 201)
        record = Record.objects.get(pk=1)
        self.assertEqual(record.title, record_dict['title'])
        self.assertEqual(record.content, record_dict['content'])

    def test_not_valid_input_returns_error_code(self):
        """test: not valid input returns error"""
        test_cases = [
            {'title': 'test title'},
            {'content': 'test content'},
            {'title': '', 'content': 'test content'},
            {'title': 'Test name', 'content': ''},
        ]
        for case in test_cases:
            response = self.client.post(self.base_url, case)
            self.assertEqual(response.status_code, 400)

    def test_update_success_change_record(self):
        """test: success delete record"""
        record = Record.objects.create(**self.record_data)
        new_record = self.record_data
        new_record['title'] = 'New title'
        response = self.client.patch(f"{self.base_url}{record.id}/", data=new_record, content_type='application/json')
        updated_record = Record.objects.first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_record.title, new_record['title'])

    def test_delete_returns_200(self):
        """test: success delete record"""
        record = Record.objects.create(**self.record_data)
        response = self.client.delete(f"{self.base_url}{record.id}/")
        self.assertEqual(response.status_code, 204)
