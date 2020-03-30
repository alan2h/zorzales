# Generated by Django 3.0.1 on 2020-03-30 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sectores', '0001_initial'),
        ('articulos', '0005_auto_20200328_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sectores.Sector'),
        ),
    ]
