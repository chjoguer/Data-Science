# Generated by Django 3.0.1 on 2020-09-25 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_caracteristicas_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caracteristicas_store',
            old_name='cpi',
            new_name='CPI',
        ),
        migrations.RenameField(
            model_name='caracteristicas_store',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='caracteristicas_store',
            old_name='fuel_price',
            new_name='Fuel_Price',
        ),
        migrations.RenameField(
            model_name='caracteristicas_store',
            old_name='isholiday',
            new_name='IsHoliday',
        ),
        migrations.RenameField(
            model_name='caracteristicas_store',
            old_name='markdown1',
            new_name='MarkDown1',
        ),
        migrations.RenameField(
            model_name='caracteristicas_store',
            old_name='markdown2',
            new_name='MarkDown2',
        ),
        migrations.RenameField(
            model_name='caracteristicas_store',
            old_name='markdown3',
            new_name='MarkDown3',
        ),
        migrations.RenameField(
            model_name='caracteristicas_store',
            old_name='markdown4',
            new_name='MarkDown4',
        ),
        migrations.RenameField(
            model_name='caracteristicas_store',
            old_name='markdown5',
            new_name='MarkDown5',
        ),
        migrations.RenameField(
            model_name='caracteristicas_store',
            old_name='id_tienda_c',
            new_name='Store',
        ),
        migrations.RenameField(
            model_name='caracteristicas_store',
            old_name='temperature',
            new_name='Temperature',
        ),
        migrations.RenameField(
            model_name='caracteristicas_store',
            old_name='unemployment',
            new_name='Unemployment',
        ),
    ]
