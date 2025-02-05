from django.db.models import BooleanField
from django.forms import ModelForm

from health.models import Client, Record


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'surname', 'phone', 'address', 'email', 'birth_date', 'created_at')


class RecordForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Record
        fields = ('client', 'record_date', 'record_time', 'doctor')
