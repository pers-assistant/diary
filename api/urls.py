from django.urls import path, include

# V1
urlpatterns = [
    path('v1/planner/', include('planner.urls'))
]