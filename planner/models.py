from django.db import models


class Record(models.Model):
    """Record instance"""

    title = models.TextField(verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
