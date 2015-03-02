from django.db import models

from taggit.managers import TaggableManager

class Project(models.Model):
    name = models.CharField(max_length=100,unique=True,blank=False)
    description = models.TextField()
    duration = models.PositiveSmallIntegerField(default=0)
    plan = models.FileField()
    furnitures = models.TextField()
    authors = models.TextField()
    history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()    

    def __str__(self):
        return self.name
