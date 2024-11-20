from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from .models import Herramienta
from .forms import HerramientaForm


# Create your views here.

class StaffRequiredMixin(object):

    """
    Este mixin requerirá que los usuarios sean miembros del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class HerramientasListView(ListView):
    model = Herramienta

class HerramientasDetailView(DetailView):
    model = Herramienta

@method_decorator(staff_member_required, name='dispatch')
class HerramientasCreate(CreateView):
    model = Herramienta
    form_class = HerramientaForm
    success_url = reverse_lazy('herramientas:herramientas')

@method_decorator(staff_member_required, name='dispatch')
class HerramientasUpdate(UpdateView):
    model = Herramienta
    form_class = HerramientaForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('herramientas:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class HerramientasDelete(DeleteView):
    model = Herramienta
    success_url = reverse_lazy("herramientas:herramientas")
