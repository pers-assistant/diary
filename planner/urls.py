from django.urls import path

from planner import views

urlpatterns = [
    path('records/<int:record_id>/', views.record)
]