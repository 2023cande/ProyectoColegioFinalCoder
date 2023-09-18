from django.shortcuts import render , redirect
from AppColegio.models import Alumno , Profesor , Entregables , Avatar
from django.http import HttpResponse
from django.template import loader
from AppColegio.forms import Alumno_Form , Profesor_Form , Entregables_Form , UserEditForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        return render(request, "padre.html" , {"url":avatares[0].imagen.url })
    else:
        return render(request, "padre.html" , {"url": None })


def alumnos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = None 

    if avatares.exists():
        url_avatar = avatares[0].imagen.url

    alumnos = Alumno.objects.all()
    return render(request, "alumnos.html", {"alumnos": alumnos, "url": url_avatar})


def profesores(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = None 

    if avatares.exists():
        url_avatar = avatares[0].imagen.url

    profesores = Profesor.objects.all()
    return render(request, "profesores.html", {"profesores": profesores, "url": url_avatar})


#def entregables(request):
      #avatares = Avatar.objects.filter(user=request.user.id)
      #return render(request, "entregables.html" , {"url":avatares[0].imagen.url})

def entregables(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = None 

    if avatares.exists():
        url_avatar = avatares[0].imagen.url

    entregables = Entregables.objects.all()
    return render(request, "entregables.html", {"entregables": entregables, "url": url_avatar})

def aboutme(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request, "aboutme.html" , {"url":avatares[0].imagen.url})

def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = Alumno_Form( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno( nombre=datos['nombre'] , apellido=datos['apellido'] , email=datos['email'] )
            alumno.save()
            return render( request , "formulario.html")
    
    return render( request , "formulario.html")


def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = Profesor_Form( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor( nombre=datos['nombre'] , apellido=datos['apellido'] , email=datos['email'] , materia=datos ['materia'] )
            profesor.save()
            return render( request , "formulario2.html")
    
    return render( request , "formulario2.html")

def entregables_formulario(request):
    if request.method == "POST":
        mi_formulario = Entregables_Form(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            fechadeentrega = datos['fechadeentrega'].strftime('%Y-%m-%d')

            entregables = Entregables(nombre=datos['nombre'], apellido=datos['apellido'], fechadeentrega=fechadeentrega)
            entregables.save()
            return render(request, "entregables.html")
    
    return render(request, "entregables.html")



def buscar_alumno(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render( request , "buscar_alumno.html" , {"url":avatares[0].imagen.url})


def alta_alumno(request, nombre , apellido , email):
    alumno = Alumno(nombre=nombre , apellido=apellido , email=email)
    alumno.save()
    texto = f"Se guardo en la BD el Alumno: {alumno.nombre} Apellido: {alumno.apellido} , Email: {alumno.email}"
    return HttpResponse(texto)

def alta_profesor(request, nombre , apellido , email , materia):
    profesor = Profesor(nombre=nombre , apellido=apellido , email=email , materia=materia)
    profesor.save()
    texto = f"Se guardo en la BD el profesor: {profesor.nombre} Apellido: {profesor.apellido} , Email: {profesor.email} , Materia: {profesor.materia}"
    return HttpResponse(texto)


def buscar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = None 

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        alumnos = Alumno.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda.html", {"alumnos": alumnos})
    else:
        return HttpResponse("Campo vacio")
    



def elimina_alumno( request , id):

    alumno = Alumno.objects.get(id=id)
    alumno.delete()

    alumno = Alumno.objects.all()

    return render(request , "alumnos.html" , {"alumnos": alumno})


def editar(request , id):

    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Alumno_Form( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos['nombre']
            alumno.apellido = datos['apellido']
            alumno.email = datos['email']
            alumno.save()

            alumno = Alumno.objects.all()          
            return render(request , "alumnos.html" , {"alumnos": alumnos})
    else:
        mi_formulario = Alumno_Form(initial={'nombre':alumno.nombre , "apellido":alumno.apellido , "email":alumno.email})
    
    return render( request , "editar_alumno.html" , {"mi_formulario":mi_formulario, "alumno": alumno})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                avatares = Avatar.objects.filter(user=request.user.id)
                if avatares.exists():
                    return render(request, "inicio.html", {"usuario": user, "url": avatares[0].imagen.url})
                else:
                    return render(request, "inicio.html", {"usuario": user, "url": None})
            else:
                return HttpResponse(f"Usuario incorrecto")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})



def register(request):

    if request.method == "POST":
       
       form = UserCreationForm(request.POST)

       if form.is_valid():
           form.save()
           return HttpResponse("Usuario creado")
    else:
        form = UserCreationForm()
    return render(request , "register.html" , {"form":form})


def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render(request , "inicio.html")

    else: 
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request , "editar_perfil.html" , {"miFormulario":miFormulario , "usuario":usuario})


