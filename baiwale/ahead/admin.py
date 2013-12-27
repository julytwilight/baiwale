# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Thing, Category


class ThingAdmin(admin.ModelAdmin):
    list_display = ('title', 'user',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'name',)


admin.site.register(Thing, ThingAdmin)
admin.site.register(Category, CategoryAdmin)