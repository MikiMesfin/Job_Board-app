from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser
from .models import Job, Application

class JobTests(APITestCase):
    def setUp(self):
        self.employer = CustomUser.objects.create_user(
            username='employer',
            password='testpass123',
            is_employer=True
        )
        self.job_seeker = CustomUser.objects.create_user(
            username='jobseeker',
            password='testpass123',
            is_job_seeker=True
        )
        
    def test_create_job(self):
        self.client.force_authenticate(user=self.employer)
        url = reverse('job-list')
        data = {
            'title': 'Software Developer',
            'description': 'Python Developer needed',
            'company_name': 'Tech Corp',
            'location': 'Remote',
            'salary': '75000.00',
            'job_type': 'Full-Time'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 1)