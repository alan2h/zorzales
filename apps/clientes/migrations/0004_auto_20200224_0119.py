# Generated by Django 3.0.1 on 2020-02-24 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20200204_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='observacion',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='baja',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
