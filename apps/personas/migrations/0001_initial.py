# Generated by Django 3.0.2 on 2020-05-30 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=3000)),
                ('apellido', models.CharField(max_length=3000)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
