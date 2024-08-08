# Generated by Django 4.1.13 on 2024-08-08 07:04

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
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('fabric', models.CharField(default='', max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='')),
                ('category', models.ManyToManyField(related_name='items', to='textile_site_app.category')),
            ],
        ),
    ]
