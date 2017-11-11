# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class PalazzoAdmin(admin.ModelAdmin):
	list_display = ('sku', 'image_tag', 'color', 'sp', 'qty', 'img1')
	search_fields = ('sku', 'upc', 'item_name')
	readonly_fields = ('image_tag', )

admin.site.register(Palazzo, PalazzoAdmin)
