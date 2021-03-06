# Generated by Django 3.0.2 on 2020-06-21 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulos', '0001_initial'),
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompraArticulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras_articulos', to='articulos.Articulo')),
            ],
            options={
                'verbose_name': 'Compra-Articulo',
                'verbose_name_plural': 'Compra-Articulos',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('precio_compra', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('observacion', models.TextField(blank=True, max_length=300, null=True)),
                ('baja', models.BooleanField(blank=True, default=False, null=True)),
                ('fecha_baja', models.DateField(blank=True, null=True)),
                ('compra_articulo', models.ManyToManyField(related_name='compras_articulos', to='compras.CompraArticulo')),
                ('pedido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.Pedido')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
    ]
