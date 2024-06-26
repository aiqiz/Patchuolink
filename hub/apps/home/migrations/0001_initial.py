# Generated by Django 3.2.6 on 2024-03-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryUpdate',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('node_id', models.IntegerField(blank=True, db_column='node_ID', null=True)),
                ('soil_temp_0', models.FloatField(blank=True, null=True)),
                ('soil_temp_10', models.FloatField(blank=True, null=True)),
                ('soil_temp_20', models.FloatField(blank=True, null=True)),
                ('soil_moisture_0', models.FloatField(blank=True, null=True)),
                ('soil_moisture_10', models.FloatField(blank=True, null=True)),
                ('soil_moisture_20', models.FloatField(blank=True, null=True)),
                ('ph_0', models.FloatField(blank=True, null=True)),
                ('ph_10', models.FloatField(blank=True, null=True)),
                ('ph_20', models.FloatField(blank=True, null=True)),
                ('light_intensity_0', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'history_update',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NodeInfo',
            fields=[
                ('node_id', models.IntegerField(db_column='node_ID', primary_key=True, serialize=False)),
                ('lat_coord', models.FloatField(blank=True, null=True)),
                ('long_coord', models.FloatField(blank=True, null=True)),
                ('time_initialized', models.TimeField(blank=True, null=True)),
                ('last_update_time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'node_info',
                'managed': False,
            },
        ),
    ]
