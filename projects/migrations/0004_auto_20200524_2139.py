# Generated by Django 3.0.6 on 2020-05-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200524_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
