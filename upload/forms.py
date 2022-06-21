from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from .models import Up_file

class Up_fileForm(forms.ModelForm):
    class Meta:
        model = Up_file
        fields = ['file_upload']
    def clean_file_upload(self):
        file = self.cleaned_data.get('file_upload', False)
        if file:
            if file.size > 20*1024*1024:
                raise ValidationError("File Must be less then 20MB")
            return file
        else:
            raise ValidationError("Couldn't read uploaded file")
