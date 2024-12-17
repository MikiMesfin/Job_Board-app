from django.db import models
from django.core.validators import MinValueValidator, FileExtensionValidator
from users.models import CustomUser

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
        validators=[MinValueValidator(0)]
    )
    job_type = models.CharField(
        max_length=50, 
        choices=[
            ('Full-Time', 'Full-Time'), 
            ('Part-Time', 'Part-Time'), 
            ('Remote', 'Remote')
        ]
    )
    posted_by = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='posted_jobs'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company_name}"

    class Meta:
        ordering = ['-created_at']

class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ]
    job = models.ForeignKey(
        Job, 
        on_delete=models.CASCADE, 
        related_name='applications'
    )
    applicant = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='applications'
    )
    resume = models.FileField(
        upload_to='resumes/',
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])
        ]
    )
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return f"{self.applicant.username}'s application for {self.job.title}"

    class Meta:
        ordering = ['-applied_at']