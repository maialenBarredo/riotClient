from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100,blank=True,null= True)
    email = models.CharField(max_length=100,blank=True,null= True)
    foto = models.URLField(max_length=200,blank=True,null= True)
    juego = models.ManyToManyField(Juego, related_name='usuarios', blank=True)
    edad = models.PositiveIntegerField(blank=True,null= True)
    pais = models.CharField(max_length=100,blank=True,null= True)
    amigos = models.ManyToManyField('self', symmetrical=False, related_name='amigos_de', blank=True)
    game_name = models.CharField(max_length=100,blank=True,null= True)
    dinero = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,blank=True,null= True)

class Juego(models.Model):
    nombre = models.CharField(max_length=100,blank=True,null= True)
    descripcion = models.TextField(blank=True,null= True)
    genero = models.CharField(max_length=100,blank=True,null= True)
    foto = models.URLField(max_length=200,blank=True,null= True)
    noticias = models.ManyToManyField('Noticia', related_name='juegos', blank=True)
    info = models.CharField(max_length=300,blank=True,null= True)
    
class Noticia(models.Model):
    nombre = models.CharField(max_length=100,blank=True,null= True)
    fecha = models.DateField(blank=True,null= True)
    contenido = models.TextField(blank=True,null= True)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name='noticias', blank=True,null= True)
    tipo = models.CharField(max_length=100,blank=True,null= True)
    foto = models.URLField(max_length=200,blank=True,null= True)