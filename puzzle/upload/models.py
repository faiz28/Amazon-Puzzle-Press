from django.db import models
import datetime

class Up_file(models.Model):
    file_upload = models.FileField(upload_to="model/file")