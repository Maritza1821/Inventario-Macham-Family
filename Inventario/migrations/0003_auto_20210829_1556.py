# Generated by Django 3.2.6 on 2021-08-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0002_rename_foto_producto1_producto_foto_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='foto_producto',
            field=models.ImageField(upload_to='static/img/productos/'),
        ),
    ]
