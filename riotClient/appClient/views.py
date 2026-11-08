from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Juego, Noticia, Icono, Usuario

# Create your views here.


# portada: los juegos y las últimas noticias
def index(request):
    juegos = Juego.objects.all()
    noticias = Noticia.objects.all()
    context = {'juegos': juegos, 'noticias': noticias}
    return render(request, 'index.html', context)


# vistas basadas en clase: lista y detalle de cada model
class JuegoListView(ListView):
    model = Juego
    context_object_name = "juegos"
    template_name = "juegos/lista_juegos.html"


class JuegoDetailView(DetailView):
    model = Juego
    context_object_name = "juego"
    template_name = "juegos/detalle_juego.html"


class NoticiaListView(ListView):
    model = Noticia
    context_object_name = "noticias"
    template_name = "noticias/lista_noticias.html"


class NoticiaDetailView(DetailView):
    model = Noticia
    context_object_name = "noticia"
    template_name = "noticias/detalle_noticia.html"


class UsuarioListView(ListView):
    model = Usuario
    context_object_name = "usuarios"
    template_name = "usuarios/lista_usuarios.html"


class UsuarioDetailView(DetailView):
    model = Usuario
    context_object_name = "usuario"
    template_name = "usuarios/detalle_usuario.html"


class IconoListView(ListView):
    model = Icono
    ordering = ['juego__nombre', 'nombre']
    context_object_name = "iconos"
    template_name = "iconos/lista_iconos.html"


class IconoDetailView(DetailView):
    model = Icono
    context_object_name = "icono"
    template_name = "iconos/detalle_icono.html"
