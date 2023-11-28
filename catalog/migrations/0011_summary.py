# Generated by Django 4.2.5 on 2023-10-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_book_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите краткое описание книги', max_length=500, verbose_name='Описание книги')),
            ],
        ),
    ]