# Generated by Django 2.1.2 on 2018-10-29 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20181029_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='rating_average',
        ),
    ]
