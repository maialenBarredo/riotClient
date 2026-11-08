from django.contrib import admin
from .models import Juego, Noticia, Icono, Servidor, Usuario, UsuarioJuego


# las filas de UsuarioJuego se ven dentro del usuario
class UsuarioJuegoInline(admin.TabularInline):
    model = UsuarioJuego
    extra = 1


class UsuarioAdmin(admin.ModelAdmin):
    inlines = [UsuarioJuegoInline]


admin.site.register(Juego)
admin.site.register(Noticia)
admin.site.register(Icono)
admin.site.register(Servidor)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(UsuarioJuego)
