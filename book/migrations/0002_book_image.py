# Generated by Django 4.1.13 on 2024-02-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
