# Generated by Django 4.2.6 on 2023-10-11 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('piscicultura', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduccionEstanque',
            fields=[
                ('idproduccion_colmena', models.AutoField(primary_key=True, serialize=False)),
                ('cant_peces', models.FloatField(blank=True, null=True)),
                ('fecha', models.CharField(max_length=45)),
                ('estanque', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='piscicultura.estanque')),
            ],
            options={
                'db_table': 'produccion_estanque',
                'managed': True,
            },
        ),
    ]
