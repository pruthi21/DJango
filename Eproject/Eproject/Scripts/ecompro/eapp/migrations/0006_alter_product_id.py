# Generated by Django 5.0.7 on 2024-10-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0005_alter_product_table_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
