from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView, UpdateView
from Log_Re.forms import FormularioLogin, FormularioRegistro, CambiarPasswordForm, ForgetPasswordForm
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


class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class RegistroView(CreateView):
    template_name = 'registro.html'
    model = Usuario
    form_class = FormularioRegistro

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email')
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})


class ForgetPassword(FormView):
    template_name = 'olvidar_clave.html'
    form_class = ForgetPasswordForm
    model = Usuario



    def form_valid(self, form):
        # Procesa los datos del formulario
        usuario = form.cleaned_data['usuario']

        # Guarda el usuario en la sesión
        self.request.session['usuario'] = usuario
        session_user = self.request.session.get('usuario')
        usr = Usuario.objects.filter(username=session_user)
        if session_user and usr:
            return redirect('clavenew')
        else:
            messages.error(self.request, '¡El usuario que intenta enviar no existe!')
            return redirect('claveolv')



class CambiarPassword(View):
    template_name = 'cambiar_clave.html'
    form_class = CambiarPasswordForm
    model = Usuario
    success_url = reverse_lazy('login')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            usuario = self.request.session.get('usuario')
            user = Usuario.objects.get(username=usuario)
            user.set_password(form.cleaned_data.get('password2'))
            user.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})



