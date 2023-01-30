from django.shortcuts import render

from django.http import HttpResponse


def record(request, record_id: int) -> HttpResponse:
    return HttpResponse(content_type='application/json')