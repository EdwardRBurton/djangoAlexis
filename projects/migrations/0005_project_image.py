# Generated by Django 3.1.3 on 2020-11-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FilePathField(default='image', path='/static/img'),
        ),
    ]
