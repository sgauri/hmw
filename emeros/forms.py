from django.contrib import admin
from .models import Palazzo
from django import forms

class PalazzoForm(ModelForm):
	color = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple(), choices = models.COLOR_CHOICES)