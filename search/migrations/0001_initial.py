# Generated by Django 4.1.13 on 2024-02-29 07:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searched', models.CharField(max_length=50)),
                ('search_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
