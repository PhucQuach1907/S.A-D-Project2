# Generated by Django 4.1.13 on 2024-03-07 07:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
