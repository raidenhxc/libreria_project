from django.contrib import admin

from libreria.models import Autor, Genero, Estanteria, Libro, UserProfile

# Register your models here.
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Estanteria)
admin.site.register(Libro)
admin.site.register(UserProfile)