# Generated by Django 3.0.1 on 2020-09-25 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20200924_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristicas_store',
            name='CPI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas_store',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas_store',
            name='Fuel_Price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas_store',
            name='IsHoliday',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas_store',
            name='MarkDown1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas_store',
            name='MarkDown2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas_store',
            name='MarkDown3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas_store',
            name='MarkDown4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas_store',
            name='MarkDown5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas_store',
            name='Temperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas_store',
            name='Unemployment',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='caracteristicas22',
            table=None,
        ),
        migrations.CreateModel(
            name='Caracteristicas_final',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(blank=True, null=True)),
                ('Temperature', models.FloatField(blank=True, null=True)),
                ('Fuel_Price', models.FloatField(blank=True, null=True)),
                ('MarkDown1', models.FloatField(blank=True, null=True)),
                ('MarkDown2', models.FloatField(blank=True, null=True)),
                ('MarkDown3', models.FloatField(blank=True, null=True)),
                ('MarkDown4', models.FloatField(blank=True, null=True)),
                ('MarkDown5', models.FloatField(blank=True, null=True)),
                ('CPI', models.FloatField(blank=True, null=True)),
                ('Unemployment', models.FloatField(blank=True, null=True)),
                ('IsHoliday', models.TextField(blank=True, null=True)),
                ('Store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Tiendas')),
            ],
        ),
    ]
