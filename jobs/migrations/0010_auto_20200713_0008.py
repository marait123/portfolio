# Generated by Django 2.2.5 on 2020-07-12 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_jobcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobcomment',
            old_name='blog_id',
            new_name='job_id',
        ),
    ]