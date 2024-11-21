from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render,  get_object_or_404
from .models import *
from .forms import *

@login_required
def home(request):
    return render(request, 'home.html')

# ----- USUARIOS -----
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'registration/leerUsu.html', {'usuarios': usuarios})

def crear_usuario(request):
    formulario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'registration/crear.html', {'formulario':formulario})

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, usuario_id=usuario_id)
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()  
            return redirect('usuarios')  
    else:
        formulario = UsuarioForm(instance=usuario)  
    return render(request, 'registration/editar.html', {'formulario': formulario})

def eliminar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(usuario_id = usuario_id)
    usuario.delete()
    return redirect('usuarios')


# ----- TICKETS -----
def tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/index.html', {'tickets': tickets})

def crear_ticket(request):
    formulario = TicketForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('tickets')
    return render(request, 'tickets/crear.html', {'formulario':formulario})

def editar_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    if request.method == 'POST':
        formulario = TicketForm(request.POST, request.FILES, instance=ticket)
        if formulario.is_valid():
            formulario.save()  
            return redirect('tickets')  
    else:
        formulario = TicketForm(instance=ticket)  
    return render(request, 'tickets/editar.html', {'formulario': formulario})

def eliminar_ticket(request, ticket_id):
    ticket = ticket.objects.get(ticket_id = ticket_id)
    ticket.delete()
    return redirect('tickets')
    
