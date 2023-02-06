from rest_framework import serializers

from planner.models import Record


class RecordSerializer(serializers.ModelSerializer):
    """Serializer for Record"""

    class Meta:
        model = Record
        fields = ('id', 'content', 'title', 'created_at')
