# Generated by Django 3.2.4 on 2021-06-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('age', models.PositiveIntegerField(default=18, verbose_name='Age')),
                ('champions', models.PositiveIntegerField(default=0, verbose_name='Champions')),
                ('champion_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Champion Name')),
            ],
        ),
    ]
