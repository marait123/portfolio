# Generated by Django 2.2.5 on 2020-01-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190916_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]
