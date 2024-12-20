from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages

from Modulos.Coordinador.Turno.models import *
from Modulos.Coordinador.Turno.forms import *
from Modulos.Login.mixin import CambiarEstadoMixin, RoleRequiredMixin

# Create your views here.

class Turn_View(LoginRequiredMixin, RoleRequiredMixin, ListView):
    model = Turno_Model
    required_role = 'Coordinador'
    context_object_name = 'turno'
    template_name = 'listado_turno.html'
    paginate_by = 5
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dirurl'] = reverse('turno:crear_turno')
        context['title_table'] = 'Listado de turnos'
        context['dir_search'] = self.request.path
        context['placeholder'] = 'Filtre por tipos de novedades'
        
        return context
    

class Turn_Create(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Turno_Model
    required_role = 'Coordinador'
    template_name = 'crear_turno.html'
    form_class = Turno_Form 
    success_url = reverse_lazy('turno:listar_turno')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Formulario: Turno'
        context['cancelar'] = reverse('turno:listar_turno')
        context['action_save'] = self.request.path
        return context
  

    def form_invalid(self, form):
        messages.error(self.request, "Por favor registrar un turno diferente a los ya creados")
        return super().form_invalid(form)


class Turno_Update(LoginRequiredMixin, RoleRequiredMixin, UpdateView):
    model = Turno_Model
    required_role = 'Coordinador'
    template_name = 'crear_turno.html'
    form_class = Turno_Form
    success_url = reverse_lazy('turno:listar_turno')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Edición de turno'
        context['cancelar'] = reverse('turno:listar_turno')
        

        return context
    
class InactivarActivarTurnoView(CambiarEstadoMixin):
    model = Turno_Model
    redirect_url = 'turno:listar_turno'  # Redirección específica para TipoNovedad_Model