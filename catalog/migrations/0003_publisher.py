# Generated by Django 4.2.5 on 2023-09-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=' Введите наименование издательства', max_length=20, verbose_name='Издательство')),
            ],
        ),
    ]
