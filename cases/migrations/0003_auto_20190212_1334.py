# Generated by Django 2.1.5 on 2019-02-12 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_auto_20190128_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='teams',
        ),
        migrations.AlterField(
            model_name='case',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
