from django.test import TestCase

from planner.models import Record

class RecordModelTest(TestCase):
    """Test: Record model"""

    def test_saving_and_retrieving_items(self):
        """test: saving and retriving records"""
        records_data = [
            {
                'title': 'First record',
                'content': 'Content for first record'
            }, {
                'title': 'Second record',
                'content': 'Content for decond record'
            }
        ]
        Record.objects.create(**records_data[0])
        Record.objects.create(**records_data[1])

        records = Record.objects.all()
        self.assertEqual(records.count(), 2)

        first_record = records[0]
        second_record = records[1]
        self.assertEqual(first_record.title, records_data[0]['title'])
        self.assertEqual(first_record.content, records_data[0]['content'])
        self.assertEqual(second_record.title, records_data[1]['title'])
        self.assertEqual(second_record.content, records_data[1]['content'])
