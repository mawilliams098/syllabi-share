# Generated by Django 3.0.6 on 2020-06-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabiShare', '0020_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
