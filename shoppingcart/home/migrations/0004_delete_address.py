# Generated by Django 3.0.6 on 2021-03-31 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
    ]