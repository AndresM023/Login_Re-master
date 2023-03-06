from django.contrib.auth.forms import AuthenticationForm
from django import forms
from Log_Re.models import Usuario


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['id'] = 'user'
        self.fields['password'].widget.attrs['id'] = 'contraseña3'


class FormularioRegistro(forms.ModelForm):
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'type': 'password',
               'id': 'contraseña',
               'required': 'required'
               }))

    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'type': 'password',
               'id': 'contra2',
               'required': 'required'
               }))

    class Meta:
        model = Usuario
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'id': 'user', 'type': 'text'}),
            'email': forms.EmailInput(attrs={'id': 'correo', 'type': 'text'}),
        }

    def clean_password2(self):
        """
        Validar contraseñas
        Método que valida que ambas contraseñas sean iguales, antes de ser encriptadas y guardadas
        en la base de datos. Se retorna la clave válida.

        Excepciones:
        ValidationError - cuando las contraseñas no son iguales muestra un mensaje de error.
        """
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las claves no coinciden')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
