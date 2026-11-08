from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

# siempre que modifico este archivo: makemigrations y migrate


class Juego(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    genero = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    # foto: url de la imagen de fondo del apartado del juego
    foto = models.URLField(max_length=200, blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    # opciones fijas para el tipo de noticia
    TIPOS = [
        ('parche', 'Parche'),
        ('actualizacion', 'Actualización'),
        ('merchandising', 'Merchandising'),
        ('evento', 'Evento'),
    ]

    nombre = models.CharField(max_length=150)
    fecha = models.DateTimeField(default=timezone.now)
    contenido = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPOS, default='parche')
    foto = models.URLField(max_length=200, blank=True, null=True)
    # un juego tiene muchas noticias
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name='noticias')

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        # las más nuevas primero
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.nombre} ({self.juego.nombre})"


class Icono(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.URLField(max_length=200)
    # si no tiene juego, es un icono general para todos
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name='iconos', blank=True, null=True)

    class Meta:
        verbose_name = "Icono"
        verbose_name_plural = "Iconos"

    def __str__(self):
        if self.juego:
            return f"{self.nombre} ({self.juego.nombre})"
        return f"{self.nombre} (general)"


class Servidor(models.Model):
    # código del servidor, por ejemplo EUW o LATAM
    nombre = models.CharField(max_length=20)
    # zona del servidor, por ejemplo Europa Oeste
    zona = models.CharField(max_length=100, blank=True, null=True)
    # cada juego tiene sus propios servidores
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name='servidores')

    class Meta:
        verbose_name = "Servidor"
        verbose_name_plural = "Servidores"
        ordering = ['nombre']
        # en un mismo juego no se repite el nombre del servidor
        constraints = [
            models.UniqueConstraint(fields=['nombre', 'juego'], name='unico_servidor_juego'),
        ]

    def __str__(self):
        return f"{self.nombre} ({self.juego.nombre})"


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    game_name = models.CharField(max_length=32)
    # el tag empieza con el código de la región, pero se puede cambiar (3 a 5 caracteres)
    tag_line = models.CharField(max_length=5, default='EUW')
    edad = models.PositiveSmallIntegerField(blank=True, null=True)
    pais = models.CharField(max_length=60, blank=True, null=True)
    # un solo saldo para todos los juegos
    dinero = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # amigos: con 'self' es simétrico, si soy tu amiga tú eres mi amigo
    amigos = models.ManyToManyField('self', blank=True)
    # juegos que tiene el usuario, pasando por la tabla intermedia UsuarioJuego
    juegos = models.ManyToManyField(Juego, through='UsuarioJuego', related_name='usuarios', blank=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        # no puede haber dos usuarios con el mismo game_name y tag_line
        constraints = [
            models.UniqueConstraint(fields=['game_name', 'tag_line'], name='unico_game_name_tag_line'),
        ]

    def __str__(self):
        return f"{self.game_name}#{self.tag_line}"


class UsuarioJuego(models.Model):
    # una fila = este usuario tiene este juego, en este servidor y con este icono
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    # cada juego tiene su servidor (el mismo usuario puede estar en otro servidor en otro juego)
    servidor = models.ForeignKey(Servidor, on_delete=models.SET_NULL, blank=True, null=True)
    icono = models.ForeignKey(Icono, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "Juego del usuario"
        verbose_name_plural = "Juegos del usuario"
        # un usuario solo puede tener una vez cada juego
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'juego'], name='unico_usuario_juego'),
        ]

    def clean(self):
        # el servidor tiene que ser del mismo juego
        if self.servidor and self.juego_id and self.servidor.juego_id != self.juego_id:
            raise ValidationError("El servidor tiene que ser de este juego.")

    def __str__(self):
        return f"{self.usuario} - {self.juego}"
