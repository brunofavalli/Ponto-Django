# -*- coding: utf-8 -*-
from django import forms
from models import Crud
from django.forms.widgets import DateInput 

class FormCrud(forms.ModelForm):
	class Meta:
		model = Crud
