# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllowedDrivers(models.Model):
    driver_id = models.IntegerField(primary_key=True)
    license_number = models.ForeignKey('Licenses', models.DO_NOTHING, db_column='license_number')
    auto_number = models.ForeignKey('Autoes', models.DO_NOTHING, db_column='auto_number')

    class Meta:
        managed = False
        db_table = 'allowed_drivers'


class Autoes(models.Model):
    auto_number = models.IntegerField(primary_key=True)
    series = models.CharField(max_length=3)
    brand = models.CharField(max_length=15)
    release_year = models.SmallIntegerField()
    price = models.IntegerField()
    product_country = models.CharField(max_length=15)
    rer_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'autoes'


class Citizens(models.Model):
    passport = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20, blank=True, null=True)
    job_place = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    license_number = models.ForeignKey('Licenses', models.DO_NOTHING, db_column='license_number', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizens'


class Damages(models.Model):
    damage_id = models.IntegerField(primary_key=True)
    assessment = models.FloatField()

    class Meta:
        managed = False
        db_table = 'damages'


class Inspectors(models.Model):
    inspector_number = models.IntegerField(primary_key=True)
    passport = models.ForeignKey(Citizens, models.DO_NOTHING, db_column='passport')
    service_period = models.SmallIntegerField()
    post = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'inspectors'


class Licenses(models.Model):
    license_number = models.IntegerField(primary_key=True)
    series = models.IntegerField()
    gibdd = models.CharField(max_length=250)
    date_issue = models.DateField()
    date_end = models.DateField()
    place_issue = models.CharField(max_length=100)
    experience = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'licenses'


class Places(models.Model):
    place_id = models.IntegerField(primary_key=True)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        managed = False
        db_table = 'places'


class ViolationTypes(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=30)
    descript = models.TextField()
    fine = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'violation_types'


class Violations(models.Model):
    violation_id = models.IntegerField(primary_key=True)
    type = models.ForeignKey(ViolationTypes, models.DO_NOTHING)
    intruder_pasp = models.ForeignKey(Citizens, models.DO_NOTHING, db_column='intruder_pasp',
                                      related_name="violations_intruder")
    witness_pasp = models.ForeignKey(Citizens, models.DO_NOTHING, db_column='witness_pasp',
                                     related_name="violations_witness", blank=True, null=True)
    victim_pasp = models.ForeignKey(Citizens, models.DO_NOTHING, db_column='victim_pasp',
                                    related_name='violations_victim', blank=True, null=True)
    inspector_number = models.ForeignKey(Inspectors, models.DO_NOTHING, db_column='inspector_number')
    damage = models.ForeignKey(Damages, models.DO_NOTHING, blank=True, null=True)
    place = models.ForeignKey(Places, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'violations'
