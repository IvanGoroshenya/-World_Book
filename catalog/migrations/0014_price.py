# Generated by Django 4.2.5 on 2023-10-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_isbn_book_isbn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.DecimalField(decimal_places=2, help_text='Введите цену книги', max_digits=7, verbose_name='Цeнa (руб.)')),
            ],
        ),
    ]
