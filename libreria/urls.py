from django.conf.urls import patterns, url
from libreria import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DeleteView
from models import Genero, Autor, Estanteria, Libro

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^autores/$', views.autores, name='autores'),
        url(r'^crear_autor', views.crear_autor, name='crear_autor'),
        url(r'^autor/(?P<autor_id>\w+)/$', views.autor, name='autor'),
        url(r'^modificar_autor/(?P<autor_id>\w+)/$', views.modificar_autor, name='modificar_autor'),
        #url(r'^borrar_autor/(?P<pk>\w+)/$', views.Borrar_autor.as_view(), name='borrar_autor'),
        url(r'^borrar_autor/(?P<pk>\w+)/$', login_required(DeleteView.as_view(model=Autor, success_url='/libreria/autores/', template_name='libreria/autor_confirm_delete.html')), name='borrar_autor'),

        url(r'^generos/$', views.generos, name='generos'),
        url(r'^crear_genero', views.crear_genero, name='crear_genero'),
        url(r'^genero/(?P<genero_id>\w+)/$', views.genero, name='genero'),
        url(r'^modificar_genero/(?P<genero_id>\w+)/$', views.modificar_genero, name='modificar_genero'),
        url(r'^borrar_genero/(?P<pk>\w+)/$', login_required(DeleteView.as_view(model=Genero, success_url='/libreria/generos/', template_name='libreria/genero_confirm_delete.html')), name='borrar_genero'),

        url(r'^estanterias/$', views.estanterias, name='estanterias'),
        url(r'^crear_estanteria', views.crear_estanteria, name='crear_estanteria'),
        url(r'^estanteria/(?P<estanteria_id>\w+)/$', views.estanteria, name='estanteria'),
        url(r'^modificar_estanteria/(?P<estanteria_id>\w+)/$', views.modificar_estanteria, name='modificar_estanteria'),
        url(r'^borrar_estanteria/(?P<pk>\w+)/$', login_required(DeleteView.as_view(model=Estanteria, success_url='/libreria/estanterias/', template_name='libreria/estanteria_confirm_delete.html')), name='borrar_estanteria'),

        url(r'^libros/$', views.libros, name='libros'),
        url(r'^crear_libro', views.crear_libro, name='crear_libro'),
        url(r'^libro/(?P<libro_id>\w+)/$', views.libro, name='libro'),
        url(r'^modificar_libro/(?P<libro_id>\w+)/$', views.modificar_libro, name='modificar_libro'),
        url(r'^borrar_libro/(?P<pk>\w+)/$', login_required(DeleteView.as_view(model=Libro, success_url='/libreria/libros/', template_name='libreria/libro_confirm_delete.html')), name='borrar_libro'),

        url(r'^registro/$', views.registro, name='registro'),
        url(r'^login/$', views.usuario_login, name='login'),
        url(r'^logout/$', views.usuario_logout, name='logout'),
        )