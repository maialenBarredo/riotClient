from django.urls import path
from . import views

urlpatterns = [
    # appClient/  (portada)
    path('', views.index, name='index'),

    # appClient/juegos/  y  appClient/juegos/1/
    path('juegos/', views.JuegoListView.as_view(), name='lista_juegos'),
    path('juegos/<int:pk>/', views.JuegoDetailView.as_view(), name='detalle_juego'),

    path('noticias/', views.NoticiaListView.as_view(), name='lista_noticias'),
    path('noticias/<int:pk>/', views.NoticiaDetailView.as_view(), name='detalle_noticia'),

    path('usuarios/', views.UsuarioListView.as_view(), name='lista_usuarios'),
    path('usuarios/<int:pk>/', views.UsuarioDetailView.as_view(), name='detalle_usuario'),

    path('iconos/', views.IconoListView.as_view(), name='lista_iconos'),
    path('iconos/<int:pk>/', views.IconoDetailView.as_view(), name='detalle_icono'),
]
