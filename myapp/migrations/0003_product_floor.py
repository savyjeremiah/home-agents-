# Generated by Django 5.1.4 on 2025-03-20 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_category_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='floor',
            field=models.IntegerField(default=0),
        ),
    ]
