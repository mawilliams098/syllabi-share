# Generated by Django 3.0.6 on 2020-05-22 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabiShare', '0008_school_uploads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='syllabus',
            field=models.FileField(blank=True, upload_to='test/'),
        ),
    ]