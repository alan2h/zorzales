# Generated by Django 3.0.2 on 2020-07-25 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabanias', '0002_auto_20200724_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabania',
            name='observacion',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]
