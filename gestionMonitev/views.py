# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gestionMonitev.models import Empresa,Pasarela,Medidor,AuthUser
import requests
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from models import *
from django.template import RequestContext
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import F
from django.contrib.auth.views import LoginView

# Create your views here.

def base(request):
    return render(request ,'base.html')

#Welcome
class WelcomeListView(LoginView):
    template_name = 'index_welcome/index.html'

#EMPRESA
def empresa_list(request):
    empresa_list = Empresa.objects.all()
    context = {'object_list': empresa_list}
    template_name='gestionMonitev/empresa_detail.html'
    return render(request,'gestionMonitev/empresa_list.html', context)

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())

class EmpresaListView(LoginRequiredMixin, ListView):
    model = Empresa

class EmpresaDetailView(LoginRequiredMixin, DetailView):
    model = Empresa

class EmpresaUpdate(UpdateView):
 login_required = True
 model = Empresa
 fields = '__all__'

class EmpresaCreate(CreateView):
 login_required = True
 model = Empresa
 fields = '__all__'

class EmpresaDelete(DeleteView):
 login_required = True
 model = Empresa
 success_url = reverse_lazy('empresa-list')

#PASARELA
def pasarela_list(request):
    pasarela_list = Pasarela.objects.all()
    context = {'object_list': pasarela_list}
    template_name='gestionMonitev/pasarela_detail.html'
    return render(request,'gestionMonitev/pasarela_list.html', context)

class PasarelaListView(LoginRequiredMixin, ListView):
    model = Pasarela

class PasarelaDetailView(LoginRequiredMixin, DetailView):
    model = Pasarela

class PasarelaUpdate(UpdateView):
 login_required = True
 model = Pasarela
 fields = '__all__'

class PasarelaCreate(CreateView):
 login_required = True
 model = Pasarela
 fields = '__all__'

class PasarelaDelete(DeleteView):
 login_required = True
 model = Pasarela
 success_url = reverse_lazy('pasarela-list')

 #MEDIDORES
def medidor_list(request):
    medidor_list = Medidor.objects.all()
    context = {'object_list': medidor_list}
    template_name='gestionMonitev/medidor_detail.html'
    return render(request,'gestionMonitev/medidor_list.html', context)

class MedidorListView(LoginRequiredMixin, ListView):
    model = Medidor

class MedidorDetailView(LoginRequiredMixin, DetailView):
    model = Medidor

class MedidorUpdate(UpdateView):
 login_required = True
 model = Medidor
 fields = '__all__'

class MedidorCreate(CreateView):
 login_required = True
 model = Medidor
 fields = '__all__'

class MedidorDelete(DeleteView):
 login_required = True
 model = Medidor
 success_url = reverse_lazy('medidor-list')

  #USUARIOS
def user_list(request):
    user_list = AuthUser.objects.all()
    context = {'object_list': user_list}
    template_name='gestionMonitev/user_detail.html'
    return render(request,'gestionMonitev/user_list.html', context)

class UserListView(LoginRequiredMixin, ListView):
    model = AuthUser

class UserDetailView(LoginRequiredMixin, DetailView):
    model = AuthUser

class UserUpdate(UpdateView):
 login_required = True
 model = AuthUser
 fields = '__all__'

class UserCreate(CreateView):
 login_required = True
 model = AuthPermission
 fields = '__all__'

class UserDelete(DeleteView):
 login_required = True
 model = AuthUser
 success_url = reverse_lazy('user-list')