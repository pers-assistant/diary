import json

from django.shortcuts import render

from django.http import HttpResponse

from planner.models import Record


def record(request, record_id: int) -> HttpResponse:
    record = Record.objects.get(pk=record_id)
    record_dict = {
        'id': record.pk,
        'title': record.title,
        'content': record.content,
        'created_at': record.сreated_at
    }
    return HttpResponse(
        json.dumps(record_dict),
        content_type='application/json'
    )
