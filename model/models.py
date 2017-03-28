
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class BrandManager(models.Manager):
    def get_by_natural_key(self, brand_name):
        return self.get(brand_name = brand_name)


class Brand(models.Model):
    brand_name = models.CharField(unique=True, max_length=50, blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'brand'


class PantsFittingManager(models.Manager):
    def get_by_natural_key(self, pfit_name):
        return self.get(pfit_name=pfit_name)


class PantsFitting(models.Model):
    pfit_name = models.CharField(max_length=20, blank=True, null=False, unique=True)
    class Meta:
        managed = True
        db_table = 'pants_fitting'


class ProductCategoryManager(models.Manager):
    def get_by_natural_key(self, category_name):
        return self.get(category_name = category_name)


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=20, blank=True, unique=True, null=True)
    class Meta:
        managed = True
        db_table = 'product_category'


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    sku = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    size_data = JSONField()
    class Meta:
        managed = True
        db_table = 'product'


class ProvincesManager(models.Manager):
    def get_by_natural_key(self, province_name):
        return self.get(province_name = province_name)


class Province(models.Model):
    province_name = models.CharField(unique=True, max_length=26, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'province'

    def __str__(self):
        return '%s' % (self.province_name)


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
    size_name = models.CharField(unique=True, max_length=15, blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'size'


class StoreManager(models.Manager):
    def get_by_natural_key(self, store_name):
        return self.get(store_name = store_name)


class Store(models.Model):
    store_name = models.CharField(unique=True, max_length=50, blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'store'


class StyleManager(models.Manager):
    def get_by_natural_key(self, style_name):
        return self.get(style_name = style_name)


class Style(models.Model):
    style_name = models.CharField(unique=True, max_length=50, blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'style'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=6, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    province = models.ForeignKey(Province, models.DO_NOTHING, db_column='province_name', blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.DateField(null=True)
    pants_fit = models.ForeignKey(PantsFitting, models.DO_NOTHING, db_column='pfit_name', blank=True, null=True)
    shirt_fit = models.ForeignKey(ShirtFitting, models.DO_NOTHING, db_column='sfit_name', blank=True, null=True)
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
    style_pref = models.ForeignKey(Style, models.DO_NOTHING, db_column='style_pref', blank=True, null=True)
    store_pref = models.ForeignKey(Store, models.DO_NOTHING, db_column='store_pref', blank=True, null=True)
    price_min = models.FloatField(blank=True, null=True)
    price_max = models.FloatField(blank=True, null=True)
    referral = models.CharField(max_length=50, blank=True, null=True)
    stripe_token = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


'''class UserUpdateForm(object):
    class Meta:
        model = User
        fields = ['first_name', 
                  'last_name', 
                  'password', 
                  'email', 
                  'address', 
                  'postal_code',
                  'city',
                  'province',
                  'country']
            
        '''