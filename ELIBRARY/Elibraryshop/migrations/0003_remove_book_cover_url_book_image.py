# Generated by Django 5.1.4 on 2025-01-17 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elibraryshop', '0002_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover_url',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='books/'),
        ),
    ]
