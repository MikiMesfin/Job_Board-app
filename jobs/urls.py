from django.urls import path
from .views import JobListView, JobDetailView, ApplicationCreateView, ApplicationListView

urlpatterns = [
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('applications/', ApplicationListView.as_view(), name='application-list'),
    path('applications/create/', ApplicationCreateView.as_view(), name='application-create'),
]
