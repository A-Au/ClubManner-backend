# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PantsFitting(models.Model):
    fit_id = models.AutoField(unique=True, blank=True, null=True)
    pfit_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pants_fitting'


class Products(models.Model):
    id = models.AutoField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Provinces(models.Model):
    province_id = models.AutoField(unique=True)
    province_name = models.CharField(unique=True, max_length=26, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provinces'


class ShirtFitting(models.Model):
    fit_id = models.AutoField(unique=True, blank=True, null=True)
    sfit_name = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shirt_fitting'


class Size(models.Model):
    size_id = models.AutoField(unique=True)
    size_name = models.CharField(unique=True, max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'size'


class Stores(models.Model):
    store_id = models.AutoField(unique=True, blank=True, null=True)
    store_name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores'


class Styles(models.Model):
    style_id = models.AutoField(unique=True)
    style_name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'styles'


class Users(models.Model):
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=6, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    province = models.ForeignKey(Provinces, models.DO_NOTHING, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    birth_month = models.IntegerField(blank=True, null=True)
    birth_day = models.IntegerField(blank=True, null=True)
    birth_year = models.IntegerField(blank=True, null=True)
    pants_fit = models.ForeignKey(PantsFitting, models.DO_NOTHING, blank=True, null=True)
    shirt_fit = models.ForeignKey(ShirtFitting, models.DO_NOTHING, blank=True, null=True)
    shirt_size = models.ForeignKey(Size, models.DO_NOTHING, db_column='shirt_size', blank=True, null=True)
    pants_size = models.IntegerField(blank=True, null=True)
    shoe_size = models.FloatField(blank=True, null=True)
    shirt_min_price = models.FloatField(blank=True, null=True)
    shirt_max_price = models.FloatField(blank=True, null=True)
    pants_min_price = models.FloatField(blank=True, null=True)
    pants_max_price = models.FloatField(blank=True, null=True)
    shoes_min_price = models.FloatField(blank=True, null=True)
    shoes_max_price = models.FloatField(blank=True, null=True)
    acces_min_price = models.FloatField(blank=True, null=True)
    acces_max_price = models.FloatField(blank=True, null=True)
    style_pref = models.ForeignKey(Styles, models.DO_NOTHING, db_column='style_pref', blank=True, null=True)
    store_pref = models.ForeignKey(Stores, models.DO_NOTHING, db_column='store_pref', blank=True, null=True)
    price_min = models.FloatField(blank=True, null=True)
    price_max = models.FloatField(blank=True, null=True)
    referral = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
