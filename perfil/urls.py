from django.urls import path
from perfil.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("login/",LoginView.as_view(template_name="pinigod/iniciar_sesion.html"), name="login"),
    path("logout/",LogoutView.as_view(template_name="pinigod/cerrar_sesion.html"), name="logout"),
    path("register/", register, name="register"),
    path("usuario/", usuarios_detail, name="usuario_detail"),
    path("usuario/change", modificar_usuario, name="usuario_change"),
]