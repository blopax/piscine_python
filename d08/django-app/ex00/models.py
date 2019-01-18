from django.db import models

# Create your models here.

class Files(models.Model):
    title = models.CharField(max_length=64, null=True)
    upload = models.FileField(upload_to='files')
