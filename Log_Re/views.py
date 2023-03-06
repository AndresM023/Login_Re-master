from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView,CreateView
from django.views.generic.edit import FormView
from Log_Re.forms import FormularioLogin, FormularioRegistro
from Log_Re.models import Usuario

# Create your views here.

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def LogoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('accounts/login/')


class MainView(TemplateView):
    template_name = 'index.html'


class RegistroView(CreateView):
    template_name = 'registro.html'
    model = Usuario
    form_class = FormularioRegistro
    success_url = reverse_lazy('login')


class ForgetPassword(TemplateView):
    template_name = 'olvidar_clave.html'

class ChangePassword(TemplateView):
    template_name = 'cambiar_clave.html'