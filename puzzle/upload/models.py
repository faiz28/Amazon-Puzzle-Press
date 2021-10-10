from django.db import models

class Document(models.Model):
    file_upload = models.FileField(upload_to='documents/%Y/%m/%d')