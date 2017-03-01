# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField


class BrandsManager(models.Manager):
    def get_by_natural_key(self, brand_name):
        return self.get(brand_name = brand_name)


class Brands(models.Model):
    #store_id = models.AutoField(unique=True, blank=True, null=True)
    brand_name = models.CharField(unique=True, max_length=50, blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'brands'


class PantsFittingManager(models.Manager):
    def get_by_natural_key(self, pfit_name):
        return self.get(pfit_name=pfit_name)


class PantsFitting(models.Model):
    #fit_id = models.AutoField(unique=True, blank=True, null=True)
    pfit_name = models.CharField(max_length=20, blank=True, null=False, unique=True)
    class Meta:
        managed = True
        db_table = 'pants_fitting'


class ProductCategoriesManager(models.Manager):
    def get_by_natural_key(self, category_name):
        return self.get(category_name = category_name)


class ProductCategories(models.Model):
    category_name = models.CharField(max_length=20, blank=True, unique=True, null=True)
    class Meta:
        managed = True
        db_table = 'product_categories'


class Products(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    brand = models.ForeignKey(Brands, models.DO_NOTHING, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    sku = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(ProductCategories, models.DO_NOTHING, blank=True, null=True)
    size_data = JSONField()
    class Meta:
        managed = True
        db_table = 'products'


class ProvincesManager(models.Manager):
    def get_by_natural_key(self, province_name):
        return self.get(province_name = province_name)


class Provinces(models.Model):
    province_name = models.CharField(unique=True, max_length=26, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'provinces'


class ShirtFittingManager(models.Manager):
    def get_by_natural_key(self, sfit_name):
        return self.get(sfit_name = sfit_name)


class ShirtFitting(models.Model):
    #fit_id = models.AutoField(unique=True, blank=True, null=True)
    sfit_name = models.CharField(unique=True, max_length=100, blank=True, null=False)
    class Meta:
        managed = True
        db_table = 'shirt_fitting'


class SizeManager(models.Manager):
    def get_by_natural_key(self, size_name):
        return self.get(size_name = size_name)


class Size(models.Model):
    #size_id = models.AutoField(unique=True)
    size_name = models.CharField(unique=True, max_length=15, blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'size'


class StoresManager(models.Manager):
    def get_by_natural_key(self, store_name):
        return self.get(store_name = store_name)


class Stores(models.Model):
    #store_id = models.AutoField(unique=True, blank=True, null=True)
    store_name = models.CharField(unique=True, max_length=50, blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'stores'


class StylesManager(models.Manager):
    def get_by_natural_key(self, style_name):
        return self.get(style_name = style_name)


class Styles(models.Model):
    #style_id = models.AutoField(unique=True)
    style_name = models.CharField(unique=True, max_length=50, blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'styles'


class Users(models.Model):
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
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
        managed = True
        db_table = 'users'
