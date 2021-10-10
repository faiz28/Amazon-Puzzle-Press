from django import forms

class DocumentForm(forms.Form):
    file_upload = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )