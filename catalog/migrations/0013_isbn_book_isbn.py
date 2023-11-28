# Generated by Django 4.2.5 on 2023-10-04 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_book_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Isbn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Должно содержать 13 символов', max_length=13, verbose_name='ISBN книги')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.ForeignKey(help_text='Должно содержать 13 символов', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.isbn', verbose_name='ISBN книги'),
        ),
    ]
