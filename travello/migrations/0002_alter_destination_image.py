# Generated by Django 5.0.6 on 2024-06-05 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.ImageField(upload_to='pics/'),
        ),
    ]
