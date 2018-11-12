# Generated by Django 2.1.2 on 2018-10-18 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181017_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=3, verbose_name='Rating (stars)'),
        ),
    ]
