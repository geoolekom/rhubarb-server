# Generated by Django 2.1.2 on 2018-11-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181101_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='rhubarbtask',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email получателя'),
        ),
    ]