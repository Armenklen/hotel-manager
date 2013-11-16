from django import forms
from django.forms import ModelForm
from models import Registro
class RegistroForm(ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	repassword=forms.CharField(widget=forms.PasswordInput)
	nombre=forms.CharField(error_messages={"required":"El nombre esta vacio"})
	ci=forms.CharField(error_messages={"required":"El ci esta vacio"})
	def clean_ci(self):
		dato=self.cleaned_data.get("ci")
		if not "pt" in dato:
			raise forms.ValidationError("Es necesario que su ci sea de potosi")
		return dato
	class Meta:
		model=Registro
		fields=["nombre","email","ci"]
class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)