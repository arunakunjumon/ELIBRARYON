# Generated by Django 5.1.4 on 2025-01-28 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elibraryshop', '0004_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='books/'),
        ),
    ]
