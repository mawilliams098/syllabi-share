# Generated by Django 3.0.6 on 2020-05-20 21:54

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('syllabiShare', '0007_suggestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='uploads',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]
