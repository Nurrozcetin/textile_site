# Generated by Django 4.1.13 on 2024-08-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textile_site_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='items', to='textile_site_app.category'),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.ManyToManyField(blank=True, related_name='items', to='textile_site_app.size'),
        ),
    ]
