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


class Projectnumber(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name


class Projectname(models.Model):
    projectnumber = models.ForeignKey(Projectnumber, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name


class Client(models.Model):
    projectnumber = models.ForeignKey(Projectnumber, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name

class Projectlocation(models.Model):
    projectnumber = models.ForeignKey(Projectnumber, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name

class Marketsector(models.Model):
    projectnumber = models.ForeignKey(Projectnumber, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name

class Memo(models.Model):
    projectnumber = models.ForeignKey(Projectnumber, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name


class Lesson(models.Model):
    projectnumber = models.ForeignKey(Projectnumber, on_delete=models.CASCADE)
    projectname = ChainedForeignKey(
        'Projectname',
        chained_field="projectnumber",
        chained_model_field="projectnumber",
        show_all=False,
        auto_choose=True
    )
    client = ChainedForeignKey(
        'Client',
        chained_field="projectnumber",
        chained_model_field="projectnumber",
        show_all=False,
        auto_choose=True
    )
    projectlocation = ChainedForeignKey(
        'Projectlocation',
        chained_field="projectnumber",
        chained_model_field="projectnumber",
        show_all=False,
        auto_choose=True
    )
    description = models.TextField()
    division = models.CharField(max_length=20)
    marketsector = ChainedForeignKey(
        'Marketsector',
        chained_field="projectnumber",
        chained_model_field="projectnumber",
        show_all=False,
        auto_choose=True
    )
    discipline = models.CharField(max_length=20)
    author = models.CharField(max_length=100)
    memo = ChainedForeignKey(
        'Memo',
        chained_field="projectnumber",
        chained_model_field="projectnumber",
        show_all=False,
        auto_choose=True,
        blank = True,
        null=True
    )
    linkfile = models.CharField(max_length=50, blank=True)
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

