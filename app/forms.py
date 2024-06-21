from django import forms
from .models import Remeras

class RemerasForm(forms.ModelForm):
    class Meta:
        model = Remeras
        fields = '__all__'

