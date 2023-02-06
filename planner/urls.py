from django.urls import path
from rest_framework import routers

from planner import views

router = routers.SimpleRouter()
router.register(r'records', views.RecordViewSet)

urlpatterns = [
]

urlpatterns += router.urls
