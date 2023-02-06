import json

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from planner.models import Record
from planner.serializers import RecordSerializer


class RecordViewSet(viewsets.ModelViewSet):
    """View for CRUD Record model"""
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

