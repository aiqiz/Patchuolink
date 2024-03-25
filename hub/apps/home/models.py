# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class HistoryUpdate(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    update_time = models.DateTimeField(blank=True, null=True)
    node_id = models.IntegerField(db_column='node_ID', blank=True, null=True)  # Field name made lowercase.
    soil_temp_0 = models.FloatField(blank=True, null=True)
    soil_temp_10 = models.FloatField(blank=True, null=True)
    soil_temp_20 = models.FloatField(blank=True, null=True)
    soil_moisture_0 = models.FloatField(blank=True, null=True)
    soil_moisture_10 = models.FloatField(blank=True, null=True)
    soil_moisture_20 = models.FloatField(blank=True, null=True)
    ph_0 = models.FloatField(blank=True, null=True)
    ph_10 = models.FloatField(blank=True, null=True)
    ph_20 = models.FloatField(blank=True, null=True)
    light_intensity_0 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'history_update'


class NodeInfo(models.Model):
    node_id = models.IntegerField(db_column='node_ID', primary_key=True)  # Field name made lowercase.
    lat_coord = models.FloatField(blank=True, null=True)
    long_coord = models.FloatField(blank=True, null=True)
    time_initialized = models.TimeField(blank=True, null=True)
    last_update_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_info'
