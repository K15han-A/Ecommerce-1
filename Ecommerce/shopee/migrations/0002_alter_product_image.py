# Generated by Django 4.1.2 on 2024-03-06 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]
