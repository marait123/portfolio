# Generated by Django 2.2.5 on 2019-09-17 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.CharField(max_length=1000),
        ),
    ]
