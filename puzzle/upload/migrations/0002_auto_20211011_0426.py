# Generated by Django 3.2.8 on 2021-10-11 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Up_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_upload', models.FileField(upload_to='2021-10-11 04:26:04.044347')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]