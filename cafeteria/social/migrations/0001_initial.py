# Generated by Django 4.0.1 on 2022-01-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=100, verbose_name='Red Social')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizacion')),
            ],
            options={
                'verbose_name': 'enlace',
                'verbose_name_plural': 'enlaces',
                'ordering': ['name'],
            },
        ),
    ]