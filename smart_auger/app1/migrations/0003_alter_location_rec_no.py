# Generated by Django 5.0.3 on 2024-04-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_location_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='rec_no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]