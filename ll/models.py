from django.db import models
from django.utils import timezone


# Create your models here.
class Project(models.Model):
    project_number = models.CharField(max_length=10)
    project_name = models.CharField(max_length=50)
    client = models.CharField(max_length=30)
    project_location = models.CharField(max_length=100)
    market_sector = models.CharField(max_length=40)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.project_number)


class Lesson(models.Model):
    project_number = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projectnumber')
    project_name = models.CharField(max_length=20)
    client = models.CharField(max_length=30)
    project_location = models.CharField(max_length=100)
    description = models.TextField()
    division = models.CharField(max_length=20)
    market_sector = models.CharField(max_length=40)
    discipline = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    link_file = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.author)