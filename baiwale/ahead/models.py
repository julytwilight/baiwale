# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from easy_thumbnails.fields import ThumbnailerImageField


class Category(models.Model):

    title      = models.CharField(max_length=30, blank=True)
    name       = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'whale_categories'


class Thing(models.Model):

    user            = models.ForeignKey(User)
    category        = models.ForeignKey(Category)
    title           = models.CharField(max_length=255, blank=True)
    shop            = models.CharField(max_length=255, blank=True)
    pic             = ThumbnailerImageField(upload_to="whale/%d/%d" % (timezone.now().year, timezone.now().month))
    post            = models.TextField()
    price           = models.FloatField(default=0)
    location        = models.CharField(max_length=255, blank=True)
    location_map    = models.CharField(max_length=255, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    last_replied_at = models.DateTimeField(auto_now=True)
    is_featured     = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'whale_things'

