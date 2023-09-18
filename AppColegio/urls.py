from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("" , views.inicio , name="inicio"),
    path("profesores" , views.profesores , name="profesores"),
    path("alumnos" , views.alumnos , name="alumnos"),
    path("entregables", views.entregables, name="entregables"),
    path("alta_alumno", views.alumno_formulario , name="alta_alumno"),
    path("alta_profesor" , views.profesor_formulario , name="alta_profesor"), 
    path("agregar_entrega" , views.entregables_formulario , name="agregar_entrega") , 
    path("buscar_alumno" , views.buscar_alumno , name="buscar_alumno"),
    path("buscar", views.buscar) , 
    path("elimina_alumno/<int:id>" , views.elimina_alumno , name="elimina_alumno"),
    path("editar_alumno/<int:id>" , views.editar , name="editar_alumno"),
    path("editar_alumno_sin_id" , views.editar ,name="editar_alumno_sin_id"),
    path("login" , views.login_request , name="login"),
    path("register" , views.register , name="register"), 
    path("logout" , LogoutView.as_view(template_name="logout.html"), name="logout") , 
    path("editarPerfil" , views.editarPerfil , name="editarPerfil") ,
    path("about" , views.aboutme , name="aboutme")
]
