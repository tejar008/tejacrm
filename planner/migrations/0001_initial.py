# Generated by Django 2.1.2 on 2019-01-08 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('contacts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Event')),
                ('event_type', models.CharField(max_length=7, verbose_name='Type of the event')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Planned', 'Planned'), ('Held', 'Held'), ('Not Held', 'Not Held'), ('Not Started', 'Not Started'), ('Started', 'Started'), ('Completed', 'Completed'), ('Canceled', 'Canceled'), ('Deferred', 'Deferred')], max_length=64, verbose_name='Status')),
                ('direction', models.CharField(blank=True, max_length=20)),
                ('start_date', models.DateTimeField(default=None)),
                ('close_date', models.DateTimeField(default=None, null=True)),
                ('duration', models.IntegerField(default=None, null=True, verbose_name='Durations')),
                ('priority', models.CharField(blank=True, max_length=10)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('assigned_to', models.ManyToManyField(blank=True, related_name='event_assigned_users', to=settings.AUTH_USER_MODEL)),
                ('attendees_contacts', models.ManyToManyField(blank=True, related_name='attendees_contact', to='contacts.Contact')),
                ('attendees_leads', models.ManyToManyField(blank=True, related_name='attendees_lead', to='leads.Lead')),
                ('attendees_user', models.ManyToManyField(blank=True, related_name='attendees_user', to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(blank=True, choices=[(10, 'Account'), (13, 'Lead'), (14, 'Opportunity'), (11, 'Case')], limit_choices_to=models.Q(models.Q(('app_label', 'account'), ('id', 10), ('model', 'Account')), models.Q(('app_label', 'leads'), ('id', 13), ('model', 'Lead')), models.Q(('app_label', 'opportunity'), ('id', 14), ('model', 'Opportunity')), models.Q(('app_label', 'cases'), ('id', 11), ('model', 'Case')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_type', models.CharField(blank=True, max_length=5, null=True)),
                ('reminder_time', models.IntegerField(blank=True, null=True, verbose_name='Reminder')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='reminders',
            field=models.ManyToManyField(blank=True, to='planner.Reminder'),
        ),
        migrations.AddField(
            model_name='event',
            name='teams',
            field=models.ManyToManyField(blank=True, to='common.Team'),
        ),
        migrations.AddField(
            model_name='event',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
