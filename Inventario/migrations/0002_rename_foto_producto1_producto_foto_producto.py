# Generated by Django 3.2.6 on 2021-08-29 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='foto_producto1',
            new_name='foto_producto',
        ),
    ]
