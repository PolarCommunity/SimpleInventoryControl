from django.forms import ModelForm
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class IngresoForm(ModelForm):
    class Meta:
        model = Ingreso
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(IngresoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['total'].widget = forms.HiddenInput()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.add_input(Submit('submit', 'Guardar'))

class IngresoDetalleForm(ModelForm):
    class Meta:
        model = DetalleIngreso
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(IngresoDetalleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['precio_total'].widget = forms.HiddenInput()
        self.fields['ingreso'].widget = forms.HiddenInput()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.add_input(Submit('submit', 'Guardar'))
