# Generated by Django 2.1.5 on 2019-01-26 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_real_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='capacity',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='driver',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='license_plate_number',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='customuser',
            name='optional_info',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='vehicle_type',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
