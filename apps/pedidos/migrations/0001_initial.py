# Generated by Django 3.0.2 on 2020-05-30 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoArticulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articulos', to='articulos.Articulo')),
            ],
            options={
                'verbose_name': 'Pedido-Articulo',
                'verbose_name_plural': 'Pedidos-Articulos',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('precio_compra', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('observacion', models.TextField(blank=True, max_length=300, null=True)),
                ('baja', models.BooleanField(blank=True, default=False, null=True)),
                ('fecha_baja', models.DateField(blank=True, null=True)),
                ('pedido_articulo', models.ManyToManyField(related_name='articulos_pedidos', to='pedidos.PedidoArticulo')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
