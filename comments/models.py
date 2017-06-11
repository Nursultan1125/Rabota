from django.db import models

# Create your models here.

class Commenst(models.Model):
    comments_title = models.CharField(max_length=10)
