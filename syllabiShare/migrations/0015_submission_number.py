# Generated by Django 3.0.6 on 2020-06-01 19:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabiShare', '0014_merge_20200528_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='number',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
