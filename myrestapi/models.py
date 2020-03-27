from django.db import models

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=500)
    project_description = models.CharField(max_length=500)
    def __str__(self):
        return self.project_title