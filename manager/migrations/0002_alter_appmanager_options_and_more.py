# Generated by Django 4.1.13 on 2024-03-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appmanager',
            options={'verbose_name': 'Manager', 'verbose_name_plural': 'Managers'},
        ),
        migrations.AlterField(
            model_name='appmanager',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='appmanager',
            name='username',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]