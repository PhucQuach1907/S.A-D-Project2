# Generated by Django 4.1.13 on 2024-03-13 03:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='book_id',
            new_name='product_id',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
