from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey, \
    ChainedManyToManyField, GroupedForeignKey

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


class Project_number(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name


class Project_name(models.Model):
    project_number = models.ForeignKey(Project_number, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name


class Client(models.Model):
    project_name = models.ForeignKey(Project_name, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name

class Project_location(models.Model):
    client = models.ForeignKey(Project_name, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name

class Market_sector(models.Model):
    project_location = models.ForeignKey(Project_name, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name

class Lesson(models.Model):
    project_number = models.ForeignKey(Project_number, on_delete=models.CASCADE)
    project_name = ChainedForeignKey(
        'Project_name',
        chained_field="project_number",
        chained_model_field="project_number",
        show_all=False,
        auto_choose=True
    )
    client = ChainedForeignKey(
        'Client',
        chained_field="project_name",
        chained_model_field="project_name",
        show_all=False,
        auto_choose=True
    )
    project_location = ChainedForeignKey(
        'Project_location',
        chained_field="client",
        chained_model_field="client",
        show_all=False,
        auto_choose=True
    )
    description = models.TextField()
    division = models.CharField(max_length=20)
    market_sector = ChainedForeignKey(
        'Market_sector',
        chained_field="project_location",
        chained_model_field="project_location",
        show_all=False,
        auto_choose=True
    )
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