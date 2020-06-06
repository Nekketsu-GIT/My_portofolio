from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="projects/")
