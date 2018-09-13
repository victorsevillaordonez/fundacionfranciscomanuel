from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .models import Evento,Galeria
import datetime
from datetime import date
from .forms import *
from .serializers import *
from rest_framework import viewsets


def history_view(request):
	return render(request,'history.html')

class Ver_imagenes_view(ListView):
	model = Galeria
	template_name = 'galeria_list.html'
	def get_queryset(self):
		return Galeria.objects.filter(evento_id=self.kwargs['evento_id'])

class EventoAnteriorListView(ListView):
	context_object_name = "evento_list"
	queryset = Evento.objects.filter(fecha_evento__range=["2000-01-01", datetime.date.today()])
	template_name = 'evento_list.html'

class EventoFuturoListView(ListView):
	context_object_name = "evento_list"
	queryset = Evento.objects.filter(fecha_evento__range=[datetime.date.today(),"3000-01-01"])
	template_name = 'evento_list.html'

class EventoListView(ListView):
	context_object_name = "evento_list"
	queryset = Evento.objects.all().order_by('-fecha_evento')
	template_name = 'evento_list.html'


class CreateEventView(LoginRequiredMixin,CreateView):
	login_url = '/login/'
	model = Evento
	form_class = Crear_event_form
	template_name = 'crear_evento_form.html'
	success_url = reverse_lazy('allLista')

class UpdateEventoView(LoginRequiredMixin,UpdateView):
	login_url = '/login/'
	model = Evento
	form_class = Crear_event_form
	template_name = 'crear_evento_form.html'
	success_url = reverse_lazy('allLista')

class DeleteEventoView(LoginRequiredMixin,DeleteView):
	login_url = '/login/'
	model = Evento
	success_url = reverse_lazy('allLista')

def login_view(request):
	usu = ""
	cla = ""
	if request.method == 'POST':
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu,password=cla)
			if usuario is not None and usuario.is_active:
				login(request,usuario)
				return render(request,'menu.html',locals())
			else:
				msj = "Usuario o clave incorrecta"
		formulario = login_form()
	return render(request,'login.html',locals())

def logout_view(request):
	logout(request)
	return render(request,'menu.html',locals())
	
def menu_view(request):
	return render(request,'menu.html',locals())

class UploadImageView(LoginRequiredMixin,CreateView):
	login_url = '/login/'
	model = Galeria
	form_class = Crear_Galeria_form
	template_name = 'crear_galeria.html'
	success_url = reverse_lazy('upload')

"""WEBSERVICES"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class GaleriaViewSet(viewsets.ModelViewSet):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
