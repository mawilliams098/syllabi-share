# Generated by Django 3.0.6 on 2020-06-02 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('syllabiShare', '0020_make_school_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='user_fk_temp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
