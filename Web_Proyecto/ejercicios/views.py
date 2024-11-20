"""from django.shortcuts import render
from .models import Ejercicio

# Create your views here.

def ejercicios (request):
    ejercicios = Ejercicio.objects.all()
    return render(request, "ejercicios/ejercicios.html", {'ejercicios':ejercicios})"""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from .models import Ejercicio
from .forms import EjercicioForm


# Create your views here.

def tipoEjercicios (request):
    return render(request, "ejercicios/tipoEjercicios.html")

class StaffRequiredMixin(object):

    """
    Este mixin requerirá que los usuarios sean miembros del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class EjerciciosListView(ListView):
    model = Ejercicio

class EjerciciosDetailView(DetailView):
    model = Ejercicio

@method_decorator(staff_member_required, name='dispatch')
class EjerciciosCreate(CreateView):
    model = Ejercicio
    form_class = EjercicioForm
    success_url = reverse_lazy('ejercicios:ejercicios')

@method_decorator(staff_member_required, name='dispatch')
class EjerciciosUpdate(UpdateView):
    model = Ejercicio
    form_class = EjercicioForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('ejercicios:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class EjerciciosDelete(DeleteView):
    model = Ejercicio
    success_url = reverse_lazy("ejercicios:ejercicios")
