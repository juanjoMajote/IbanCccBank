from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from .models import Client
from .forms import CreatedFormsClient
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.


class Index(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = ('userBank.view_client')
    model = Client
    #context_object_name = 'clients'
    template_name = 'core/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.filter(userCreated=self.request.user.id)
        return context

class ClientDetailView(PermissionRequiredMixin,LoginRequiredMixin,BSModalReadView):
    permission_required = ('userBank.view_client')
    model = Client
    template_name = 'userBank/read_client.html'

class ClientCreateView(PermissionRequiredMixin,LoginRequiredMixin,BSModalCreateView):
    permission_required = ('userBank.add_client')
    model = Client
    form_class = CreatedFormsClient
    template_name = 'userBank/create_client.html'
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        form.instance.userCreated = self.request.user
        return super().form_valid(form)


class ClientUpdateView(PermissionRequiredMixin,LoginRequiredMixin,BSModalUpdateView):
    permission_required = ('userBank.change_client')
    model = Client
    form_class = CreatedFormsClient
    template_name = 'userBank/update_client.html'
    success_url = reverse_lazy('index')

class ClientDeleteView(BSModalDeleteView):
    model = Client
    template_name ='userBank/delete_client.html'
    success_message = "Client was deleted successfully."
    success_url = reverse_lazy('index')



class UserDetailView(DetailView):
    model = User
    template_name = 'userBank/user_details.html'
