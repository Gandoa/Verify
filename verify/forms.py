from django import forms
from django.forms import ModelForm
from .models import *


class Verify_Code(ModelForm):
	class Meta:
		model = User_verify
		fields = ("code", "number")