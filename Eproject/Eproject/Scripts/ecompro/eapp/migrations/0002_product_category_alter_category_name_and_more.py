# Generated by Django 5.1.1 on 2024-09-24 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='abc', on_delete=django.db.models.deletion.CASCADE, to='eapp.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='abc', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='discreption',
            field=models.TextField(default='abc', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='abc', upload_to='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='abc', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]
