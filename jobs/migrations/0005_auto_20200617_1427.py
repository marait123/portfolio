# Generated by Django 2.2.5 on 2020-06-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20200617_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interests',
            name='summary',
            field=models.CharField(default='title default', max_length=200),
        ),
        migrations.AlterField(
            model_name='interests',
            name='title',
            field=models.CharField(default='title default', max_length=100),
        ),
    ]
