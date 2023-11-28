# Generated by Django 4.2.5 on 2023-10-04 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_year_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.ForeignKey(help_text='Введите год названия', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.year', verbose_name='Год издания'),
        ),
    ]
