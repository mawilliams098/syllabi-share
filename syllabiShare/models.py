from django.db import models
from django.utils import timezone

class Submission(models.Model):
    user = models.TextField()
    prof = models.TextField()
    course = models.TextField()
    school = models.TextField()
    upvotes = models.IntegerField
    add_date = models.DateTimeField('date added', default=timezone.now)

class School(models.Model):
    school = models.TextField(unique=True, blank=True)
    domain = models.TextField(unique=True)