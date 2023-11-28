# Generated by Django 4.2.5 on 2023-10-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_alter_summary_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(help_text='Введите краткое описание книги', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='name',
            field=models.TextField(help_text='Введите краткое описание книги', max_length=500, verbose_name='Описание'),
        ),
    ]
