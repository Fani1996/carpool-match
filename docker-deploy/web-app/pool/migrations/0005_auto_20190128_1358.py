# Generated by Django 2.1.5 on 2019-01-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0004_ride_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='searchFromDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('vehicle_type', models.CharField(max_length=200)),
                ('special_request', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='searchFromSharer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('passenger_count', models.PositiveIntegerField()),
                ('vehicle_type', models.CharField(choices=[('', 'Vehicle Type'), ('1', 'Uber X'), ('2', 'Uber XL'), ('3', 'Uber XLL')], max_length=1)),
                ('special_request', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='ride',
            name='vehicle_type',
            field=models.CharField(choices=[('', 'Vehicle Type'), ('1', 'Uber X'), ('2', 'Uber XL'), ('3', 'Uber XLL')], max_length=1),
        ),
    ]