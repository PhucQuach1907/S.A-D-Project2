# Generated by Django 4.1.13 on 2024-03-27 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0003_alter_mobile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=18),
        ),
    ]
