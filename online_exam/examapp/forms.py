from django import forms
from .models import *


class profileform(forms.ModelForm):
    class Meta:
        model=profile
        fields=["name",'gender','mob','username']

