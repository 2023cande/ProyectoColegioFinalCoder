from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Alumno_Form(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class Profesor_Form(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    materia= forms.CharField(max_length=30)


class Entregables_Form(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    fechaDeEntrega = forms.DateField()  


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email' , 'password1' , 'password2']
        help_text = {k:"" for k in fields} 
        