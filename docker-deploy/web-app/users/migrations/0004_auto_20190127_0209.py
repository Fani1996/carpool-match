# Generated by Django 2.1.5 on 2019-01-27 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190126_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
