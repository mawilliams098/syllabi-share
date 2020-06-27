# Generated by Django 3.0.6 on 2020-06-02 02:43

from django.db import migrations


def populate_school_fk_for_submission(apps, schema_editor):
    # Use the historical versions
    Submission = apps.get_model('syllabiShare', 'Submission')
    School = apps.get_model('syllabiShare', 'School')
    for submission in Submission.objects.all():
        submission.school_fk_temp = School.objects.get(domain=submission.school)
        submission.save()


class Migration(migrations.Migration):

    dependencies = [
        ('syllabiShare', '0017_submission_school_fk_temp'),
    ]

    operations = [
        migrations.RunPython(populate_school_fk_for_submission)
    ]
