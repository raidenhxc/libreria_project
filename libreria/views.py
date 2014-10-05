# -*- encoding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from libreria.models import Autor, Genero, Estanteria, Libro
from libreria.forms import crear_autor_form, crear_genero_form, crear_estanteria_form, crear_libro_form, registro_form
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required


def encode_url(str):
    return str.replace(' ', '_')


def decode_url(str):
    return str.replace('_', ' ')


def index(request):
    context = RequestContext(request)
    context_dict = {'prueba': 'prueba'}

    return render_to_response('libreria/index.html', context_dict, context)


# ##########
# AUTORES #
###########
@login_required
def autores(request):
    context = RequestContext(request)

    autores_lista = Autor.objects.order_by('apellidos')
    context_dict = {'autores': autores_lista}

    return render_to_response('libreria/autores.html', context_dict, context)


@login_required
def autor(request, autor_id):
    context = RequestContext(request)

    autor = Autor.objects.get(id=autor_id)
    context_dict = {'autor_nombre': autor.nombre}
    context_dict = {'autor_id': autor.id}

    libros = Libro.objects.filter(autor=autor_id)
    context_dict['libros'] = libros

    try:
        autor = Autor.objects.get(id=autor_id)
        context_dict['autor'] = autor
    except Autor.DoesNotExist:
        pass

    return render_to_response('libreria/autor.html', context_dict, context)


@login_required
def crear_autor(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = crear_autor_form(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return autores(request)
        else:
            print form.errors
    else:
        form = crear_autor_form()

    return render_to_response('libreria/crear_autor.html', {'form': form}, context)


@login_required
def modificar_autor(request, autor_id=None):
    context = RequestContext(request)

    if autor_id:
        autor = get_object_or_404(Autor, id=autor_id)

    if request.method == 'POST':
        form = crear_autor_form(request.POST, instance=autor)
        if form.is_valid():
            form.save(commit=True)

            return autores(request)
        else:
            print form.errors
    else:
        form = crear_autor_form(instance=autor)

    return render_to_response('libreria/crear_autor.html', {'form': form, 'autor': autor}, context)


@login_required
class Borrar_autor(DeleteView):
    model = Autor
    success_url = reverse_lazy('autores')



###########
# GENEROS #
###########
@login_required
def generos(request):
    context = RequestContext(request)

    generos_lista = Genero.objects.order_by('nombre')
    context_dict = {'generos': generos_lista}

    return render_to_response('libreria/generos.html', context_dict, context)


@login_required
def genero(request, genero_id):
    context = RequestContext(request)

    genero = Genero.objects.get(id=genero_id)
    context_dict = {'genero_nombre': genero.nombre}
    context_dict = {'genero_id': genero.id}

    libros = Libro.objects.filter(genero=genero_id)
    context_dict['libros'] = libros

    try:
        genero = Genero.objects.get(id=genero_id)
        context_dict['genero'] = genero
    except Genero.DoesNotExist:
        pass

    return render_to_response('libreria/genero.html', context_dict, context)


@login_required
def crear_genero(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = crear_genero_form(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return generos(request)
        else:
            print form.errors
    else:
        form = crear_genero_form()

    return render_to_response('libreria/crear_genero.html', {'form': form}, context)


@login_required
def modificar_genero(request, genero_id=None):
    context = RequestContext(request)

    if genero_id:
        genero = get_object_or_404(Genero, id=genero_id)

    if request.method == 'POST':
        form = crear_genero_form(request.POST, instance=genero)
        if form.is_valid():
            form.save(commit=True)

            return generos(request)
        else:
            print form.errors
    else:
        form = crear_genero_form(instance=genero)

    return render_to_response('libreria/crear_genero.html', {'form': form, 'genero': genero}, context)


@login_required
class Borrar_genero(DeleteView):
    model = Genero
    print "test"
    success_url = reverse_lazy('generos')


###############
# ESTANTERIAS #
###############
@login_required
def estanterias(request):
    context = RequestContext(request)

    estanterias_lista = Estanteria.objects.order_by('nombre')
    context_dict = {'estanterias': estanterias_lista}

    return render_to_response('libreria/estanterias.html', context_dict, context)


@login_required
def estanteria(request, estanteria_id):
    context = RequestContext(request)

    estanteria = Estanteria.objects.get(id=estanteria_id)
    context_dict = {'estanteria_nombre': estanteria.nombre}
    context_dict = {'estanteria_id': estanteria.id}

    libros = Libro.objects.filter(estanteria=estanteria_id)
    context_dict['libros'] = libros

    try:
        estanteria = Estanteria.objects.get(id=estanteria_id)
        context_dict['estanteria'] = estanteria
    except Estanteria.DoesNotExist:
        pass

    return render_to_response('libreria/estanteria.html', context_dict, context)


@login_required
def crear_estanteria(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = crear_estanteria_form(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return estanterias(request)
        else:
            print form.errors
    else:
        form = crear_estanteria_form()

    return render_to_response('libreria/crear_estanteria.html', {'form': form}, context)


@login_required
def modificar_estanteria(request, estanteria_id=None):
    context = RequestContext(request)

    if estanteria_id:
        estanteria = get_object_or_404(Estanteria, id=estanteria_id)

    if request.method == 'POST':
        form = crear_estanteria_form(request.POST, instance=estanteria)
        if form.is_valid():
            form.save(commit=True)

            return estanterias(request)
        else:
            print form.errors
    else:
        form = crear_estanteria_form(instance=estanteria)

    return render_to_response('libreria/crear_estanteria.html', {'form': form, 'estanteria': estanteria}, context)


@login_required
class Borrar_estanteria(DeleteView):
    model = Estanteria
    success_url = reverse_lazy('estanterias')


##########
# LIBROS #
##########
@login_required
def libros(request):
    context = RequestContext(request)

    libros_lista = Libro.objects.order_by('nombre')
    context_dict = {'libros': libros_lista}

    return render_to_response('libreria/libros.html', context_dict, context)


@login_required
def libro(request, libro_id):
    context = RequestContext(request)

    libro = Libro.objects.get(id=libro_id)
    context_dict = {'libro_nombre': libro.nombre}
    context_dict = {'libro_id': libro.id}

    try:
        libro = Libro.objects.get(id=libro_id)
        context_dict['libro'] = libro
    except Libro.DoesNotExist:
        pass

    return render_to_response('libreria/libro.html', context_dict, context)


@login_required
def crear_libro(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = crear_libro_form(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return libros(request)
        else:
            print form.errors
    else:
        form = crear_libro_form()

    return render_to_response('libreria/crear_libro.html', {'form': form}, context)


@login_required
def modificar_libro(request, libro_id=None):
    context = RequestContext(request)

    if libro_id:
        libro = get_object_or_404(Libro, id=libro_id)

    if request.method == 'POST':
        form = crear_libro_form(request.POST, instance=libro)
        if form.is_valid():
            form.save(commit=True)

            return libros(request)
        else:
            print form.errors
    else:
        form = crear_libro_form(instance=libro)

    return render_to_response('libreria/crear_libro.html', {'form': form, 'libro': libro}, context)


@login_required
class Borrar_libro(DeleteView):
    model = Libro
    success_url = reverse_lazy('libros')


############
# USUARIOS #
############
def registro(request):
    context = RequestContext(request)

    registrado = False

    if request.method == 'POST':
        form = registro_form(data=request.POST)

        if form.is_valid():
            user = form.save()

            user.set_password(user.password)
            user.save()

            registrado = True
        else:
            print form.errors
    else:
        form = registro_form()

    return render_to_response("libreria/registro.html", {'form': form, 'registrado': registrado}, context)


def usuario_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        nombre = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(username=nombre, password=password)

        if usuario:
            if usuario.is_active:
                login(request, usuario)
                return HttpResponseRedirect('/libreria')
            else:
                return HttpResponse("Cuenta desactivada.")
        else:
            print "Login incorrecto: {0}, {1}".format(nombre, password)
            return HttpResponse("Datos erroneos.")
    else:
        return render_to_response('libreria/login.html', context)


@login_required
def usuario_logout(request):
    logout(request)
    return HttpResponseRedirect('/libreria/')