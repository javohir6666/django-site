# Generated by Django 3.2.7 on 2021-09-18 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-add_time'], 'verbose_name_plural': 'News'},
        ),
    ]
