# Generated by Django 3.1.3 on 2020-11-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True, max_length=10, verbose_name='date')),
                ('start_time', models.DateTimeField(db_index=True, max_length=5, verbose_name='start_time')),
                ('end_time', models.DateTimeField(db_index=True, max_length=5, verbose_name='end_time')),
                ('meeting_url', models.URLField(db_index=True, verbose_name='meeting_url')),
            ],
        ),
    ]
