# Generated by Django 5.1.1 on 2024-09-24 13:55

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
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('discreption', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='image')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.category')),
            ],
        ),
    ]
