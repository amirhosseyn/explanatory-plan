from django.forms import ModelForm
from django import forms
from .models import Plan

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'