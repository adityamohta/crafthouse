from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save, pre_save


class Slider(models.Model):
    heading = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    starting_price = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.heading


def background_image_upload_to(instance, filename):
    file_extension = filename.split('.')[-1]
    new_filename = "%s.%s" % ("slider_background", file_extension)
    return "slider/background/%s" % new_filename


def service_background_image_upload_to(instance, filename):
    file_extension = filename.split('.')[-1]
    new_filename = "%s.%s" % ("service_background", file_extension)
    return "service/background/%s" % new_filename


def gallery_image_upload_to(instance, filename):
    file_extension = filename.split('.')[-1]
    new_filename = "%s.%s" % ("gallery_img", file_extension)
    return "gallery/%s" % new_filename


class SliderBackground(models.Model):
    image = models.ImageField(upload_to=background_image_upload_to)

    def __unicode__(self):
        return self.image.url


class ServiceBackground(models.Model):
    heading = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=service_background_image_upload_to)

    def __unicode__(self):
        return self.image.url


class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=gallery_image_upload_to)

    def __unicode__(self):
        return self.image.url


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=0, max_digits=10, null=True, blank=True)
    sale_price = models.DecimalField(decimal_places=0, max_digits=10, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio:product_detail", kwargs={'id': self.id})


def product_save_receiver(sender, instance, *args, **kwargs):
    product = instance
    price = product.price
    discount = product.discount
    if discount is not None:
        sale_price = price - (price * discount / 100)
    else:
        sale_price = None
    product.sale_price = sale_price
    # product.save()


pre_save.connect(product_save_receiver, sender=Product)


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to="products/%Y/%m/%d/")

def product_image_upload_to(instance, filename):
    title = instance.product.title
    return "products/%s/%s" % (title, filename)


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to=product_image_upload_to)


    def __unicode__(self):
        return self.product.title


class About(models.Model):
    text_left = models.TextField(null=True, blank=True)
    text_right = models.TextField(null=True, blank=True)


class Member(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    business_email = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="members/%Y/%m/%d/", null=True, blank=True)

    def __unicode__(self):
        return name
