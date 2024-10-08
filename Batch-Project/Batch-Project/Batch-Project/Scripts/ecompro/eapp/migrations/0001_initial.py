# Generated by Django 5.1 on 2024-09-24 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, default='', max_length=300, null=True)),
                ('image', models.ImageField(upload_to='image')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.category')),
            ],
        ),
    ]
