# Generated by Django 2.1.2 on 2018-11-01 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rhubarbtask',
            name='result',
            field=models.TextField(blank=True, null=True, verbose_name='результат выполнения'),
        ),
    ]
