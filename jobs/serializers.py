from rest_framework import serializers
from .models import Job, Application

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'company_name', 
                 'location', 'salary', 'job_type', 'created_at']
        read_only_fields = ['posted_by', 'created_at']  # Make posted_by read-only

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
