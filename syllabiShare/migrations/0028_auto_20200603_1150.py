# Generated by Django 3.0.6 on 2020-06-03 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('syllabiShare', '0027_remove_school_uploads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='syllabiShare.School'),
        ),
    ]
