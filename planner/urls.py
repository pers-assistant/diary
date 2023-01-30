from django.urls import path

from planner import views

urlpatterns = [
    path('records/', views.record)
]