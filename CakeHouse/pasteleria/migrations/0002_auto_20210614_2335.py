# Generated by Django 3.2.3 on 2021-06-15 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pasteleria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='ciudad',
            new_name='comuna',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='rut',
            new_name='cliente',
        ),
    ]
