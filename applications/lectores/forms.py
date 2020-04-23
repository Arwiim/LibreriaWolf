from django import forms
from .models import Prestamos
from applications.libros.models import Libros

class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamos
        fields = (
            'lector',
            'libro',
        )

class MultiplePrestamoForm(forms.ModelForm):

    libros = forms.ModelMultipleChoiceField( #va un conjunto relacionado al modelode la db libros
        queryset=None,
        required=True, #al menos 1 libro me tiene que mandar
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Prestamos
        fields = (
            'lector',
        )
    
    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        self.fields['libros'].queryset = Libros.objects.all()