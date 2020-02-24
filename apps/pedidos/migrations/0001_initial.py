# Generated by Django 3.0.1 on 2020-02-24 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulos', '0004_auto_20200224_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('precio_compra', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('observacion', models.TextField(blank=True, max_length=300, null=True)),
                ('articulos', models.ManyToManyField(related_name='articulos_pedidos', to='articulos.Articulo')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]