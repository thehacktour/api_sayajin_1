# Generated by Django 3.2.4 on 2021-06-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0002_alter_managersmodel_champion_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managersmodel',
            name='champion_name',
            field=models.CharField(max_length=255, verbose_name='Champion Name'),
        ),
    ]
