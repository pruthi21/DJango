# Generated by Django 5.0.7 on 2024-10-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0007_product_category_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discreption',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
