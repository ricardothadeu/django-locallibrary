# Generated by Django 4.0.1 on 2022-03-24 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_book_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
