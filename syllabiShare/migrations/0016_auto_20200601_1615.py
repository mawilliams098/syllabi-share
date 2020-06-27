# Generated by Django 3.0.6 on 2020-06-01 20:15

from django.db import migrations


def populate_number_from_course(apps, schema_editor):
    # Use the historical version of Submission
    Submission = apps.get_model('syllabiShare', 'Submission')
    for submission in Submission.objects.all():
        submission.number = int(submission.course.split()[1])
        submission.save()


class Migration(migrations.Migration):

    dependencies = [
        ('syllabiShare', '0015_submission_number'),
    ]

    operations = [
        migrations.RunPython(populate_number_from_course),
    ]