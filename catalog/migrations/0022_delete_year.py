# Generated by Django 4.2.5 on 2023-10-04 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_bookinstance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Year',
        ),
    ]
