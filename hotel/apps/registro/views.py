from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import Registro
from forms import RegistroForm,LoginForm
import datetime
# Create your views here.
def bienvenido(request):
	try:
		valor=request.session["conectado"]
	except:
		valor=False
	if valor:
		return render_to_response("bienvenido.html",
			{"username":request.session["username"]},
			RequestContext(request))
	else:
		return HttpResponseRedirect("/registro/login/")	
def autenticacion(request):
	if request.method=="POST":
		form=LoginForm(request.POST)
		if form.is_valid():
			nick=form.cleaned_data["username"]
			password=form.cleaned_data["password"]
			r=Registro.objects.get(nombre=nick,password=password)
			if r:
				request.session["conectado"]=True
				request.session["username"]=nick
				return HttpResponseRedirect("/usuario/bienvenido/")
	else:	
		form=LoginForm()
	return render_to_response("login.html",{"form":form},RequestContext(request))
def exito(request):
	return render_to_response("exito.html",{},RequestContext(request))
def login(request):
	if request.method=="POST":
		form=RegistroForm(request.POST)
		if form.is_valid():
			p=Registro(
				nombre=form.cleaned_data["nombre"],
				email=form.cleaned_data["email"],
				password=form.cleaned_data["password"],
				fecha=datetime.datetime.now().date(),
				hora=datetime.datetime.now().time()
				)
			p.save()
			return HttpResponseRedirect("/registro/exito/")
	
	else:
		form=RegistroForm()
	return render_to_response("index.html",{"miregistro":form},RequestContext(request))

