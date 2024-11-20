from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from .models import Habito
from .forms import HabitoForm


# Create your views here.

class StaffRequiredMixin(object):

    """
    Este mixin requerirá que los usuarios sean miembros del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class HabitosListView(ListView):
    model = Habito

class HabitosDetailView(DetailView):
    model = Habito

@method_decorator(staff_member_required, name='dispatch')
class HabitosCreate(CreateView):
    model = Habito
    form_class = HabitoForm
    success_url = reverse_lazy('habitos:habitos')

@method_decorator(staff_member_required, name='dispatch')
class HabitosUpdate(UpdateView):
    model = Habito
    form_class = HabitoForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('habitos:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class HabitosDelete(DeleteView):
    model = Habito
    success_url = reverse_lazy("habitos:habitos")
