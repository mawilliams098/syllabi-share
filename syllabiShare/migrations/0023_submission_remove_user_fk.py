# Generated by Django 3.0.6 on 2020-06-02 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabiShare', '0022_populate_user_fk_for_submission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='user',
        ),
        migrations.RenameField(
            model_name='submission',
            old_name='user_fk_temp',
            new_name='user',
        ),
    ]
