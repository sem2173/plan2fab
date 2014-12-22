from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100,unique=True,blank=False)
    description = models.TextField()
    duration = models.PositiveSmallIntegerField()
    plan = models.FileField()
    furnitures = models.TextField()
    authors = models.TextField()
    history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

