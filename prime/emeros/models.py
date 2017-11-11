from __future__ import unicode_literals
from django.db import models
from django.utils.safestring import mark_safe

SIZE_CHOICES = (
	("M", "M"),
	("XL", "XL"),
	("XXL", "XXL"),
)

MATERIAL_CHOICES = (
	("Crepe", 'Crepe'),
	("Cotton", 'Cotton'),
)

COLOR_CHOICES = (('White', 'White'), ("Black", "Black"), ("Green", "Green"), ("Blue", "Blue"), )

class Palazzo(models.Model):
	sku = models.SlugField()
	item_name = models.CharField(max_length=200, default='Palazzo')
	upc = models.BigIntegerField(blank=True, default='0123456789')
	description = models.TextField(default = "Write here")
	material = models.CharField(max_length=15, default='Crepe', choices=MATERIAL_CHOICES)
	color = models.CharField(max_length=50, blank=True, choices = COLOR_CHOICES, default='default')
	brand = models.CharField(max_length=10, default="Emeros")
	mrp = models.IntegerField(default=899)
	sp = models.IntegerField(default=399)
	qty = models.PositiveIntegerField(blank=True, default='5')
	package_num = models.IntegerField(blank=True, default='1')
	num_of_items = models.IntegerField(blank=True, default='1')
	package_weight = models.FloatField(blank=True, default='0.25')
	key_feature1 = models.CharField(max_length=50, default='write here')
	key_feature2 = models.CharField(max_length=50, default='write here')
	key_feature3 = models.CharField(max_length=50, default='write here')
	key_feature4 = models.CharField(max_length=50, default='write here')
	key_feature5 = models.CharField(max_length=50, default='write here')
	keywords = models.CharField(max_length=200, default='write here')
	img1 = models.ImageField(default='add image')

	def image_tag(self):
		return mark_safe('<img src="/directory/%s width = "100" height = "100" />' % (self.img1.url))

	image_tag.short_description = 'Image'
	# image_tag.allow_tags = True

	pack_length = models.PositiveIntegerField(blank=True, default='20')
	pack_width = models.PositiveIntegerField(blank=True, default='20')
	pack_height = models.PositiveIntegerField(blank=True, default='5')
	country = models.CharField(max_length=10, default="India")
	ideal_for = models.CharField(max_length=10, default='female')
	size = models.CharField(max_length=10, choices = SIZE_CHOICES, default='XL')
	occasion = models.CharField(max_length=50, default="Casual")

	def __str__(self):
		return self.sku
