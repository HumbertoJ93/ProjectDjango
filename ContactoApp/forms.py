from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, required=True)
    correo = forms.EmailField(label='Email', max_length=100, required=True)
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea, max_length=500, required=True)