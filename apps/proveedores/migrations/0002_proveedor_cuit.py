# Generated by Django 3.0.2 on 2020-06-23 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='cuit',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
