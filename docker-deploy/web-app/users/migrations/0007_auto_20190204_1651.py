# Generated by Django 2.1.5 on 2019-02-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190203_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='real_name',
            field=models.CharField(max_length=120),
        ),
    ]
