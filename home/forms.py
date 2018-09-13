from django import forms
from .models import Evento,Galeria

class Crear_event_form(forms.ModelForm):
	class Meta:
		model = Evento
		fields = '__all__'

class login_form(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput())
	clave = forms.CharField(widget=forms.PasswordInput(render_value=False))

class Crear_Galeria_form(forms.ModelForm):
	class Meta:
		model = Galeria
		fields = '__all__'