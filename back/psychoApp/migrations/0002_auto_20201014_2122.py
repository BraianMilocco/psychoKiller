# Generated by Django 3.1.2 on 2020-10-15 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='link',
            field=models.CharField(max_length=30, unique=True, verbose_name='Link'),
        ),
    ]
