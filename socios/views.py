from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Socio
from .forms import SocioForm


class SocioListView(ListView):
    model = Socio
    template_name = 'socios/socio_list.html'
    context_object_name = 'socios'

    def get_queryset(self):
        return Socio.objects.select_related('plan').order_by('nombre')


class SocioDetailView(DetailView):
    model = Socio
    template_name = 'socios/socio_detail.html'
    context_object_name = 'socio'


class SocioCreateView(CreateView):
    model = Socio
    form_class = SocioForm
    template_name = 'socios/socio_form.html'
    success_url = reverse_lazy('socio_list')


class SocioUpdateView(UpdateView):
    model = Socio
    form_class = SocioForm
    template_name = 'socios/socio_form.html'
    success_url = reverse_lazy('socio_list')


class SocioDeleteView(DeleteView):
    model = Socio
    template_name = 'socios/socio_confirm_delete.html'
    success_url = reverse_lazy('socio_list')
