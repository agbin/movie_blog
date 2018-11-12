# Generated by Django 2.1.2 on 2018-10-29 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_rating_average'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]