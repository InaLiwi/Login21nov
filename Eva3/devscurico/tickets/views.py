from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db.models import Avg, Count, F
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from .models import Ticket, Comentario, Cliente
from .forms import TicketForm, ComentarioForm

@login_required
def inicio(request):
    return render(request, 'tickets/inicio.html')

@login_required
@permission_required('tickets.view_ticket', raise_exception=True)
def lista_tickets(request):
    # Vista para listar todos los tickets
    tickets = Ticket.objects.all()
    return render(request, 'tickets/lista_tickets.html', {'tickets': tickets})

@login_required
@permission_required('tickets.view_ticket', raise_exception=True)
def detalle_ticket(request, ticket_id):
    # Vista para ver los detalles de un ticket específico y añadir comentarios
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.ticket = ticket
            comentario.autor = request.user
            comentario.save()
            return redirect('detalle_ticket', ticket_id=ticket.id)
    else:
        form = ComentarioForm()
    return render(request, 'tickets/detalle_ticket.html', {'ticket': ticket, 'form': form})

@login_required
@permission_required('tickets.add_ticket', raise_exception=True)
def crear_ticket(request):
    # Vista para crear un nuevo ticket
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.tecnico_asignado = request.user
            ticket.save()
            return redirect('lista_tickets')
    else:
        form = TicketForm()
    return render(request, 'tickets/crear_ticket.html', {'form': form})

@login_required
@permission_required('tickets.change_ticket', raise_exception=True)
def actualizar_ticket(request, ticket_id):
    # Vista para actualizar un ticket existente
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            return redirect('detalle_ticket', ticket_id=ticket.id)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/actualizar_ticket.html', {'form': form, 'ticket': ticket})

@login_required
@permission_required('tickets.delete_ticket', raise_exception=True)
def eliminar_ticket(request, ticket_id):
    # Vista para eliminar un ticket
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('lista_tickets')
    return render(request, 'tickets/eliminar_ticket.html', {'ticket': ticket})

@login_required
@permission_required('tickets.view_ticket', raise_exception=True)
def informes(request):
    # Vista para generar informes, solo accesible por administradores
    if not request.user.groups.filter(name='Administradores').exists():
        raise PermissionDenied
    
    # Cálculo de estadísticas para el informe
    total_tickets = Ticket.objects.count()
    tickets_resueltos = Ticket.objects.filter(estado='RE').count()
    tiempo_promedio_resolucion = Ticket.objects.filter(estado='RE').aggregate(
        avg_time=Avg(F('fecha_resolucion') - F('fecha_creacion'))
    )['avg_time']
    tickets_por_tecnico = Ticket.objects.values('tecnico_asignado__username').annotate(
        total=Count('id')
    )

    context = {
        'total_tickets': total_tickets,
        'tickets_resueltos': tickets_resueltos,
        'tiempo_promedio_resolucion': tiempo_promedio_resolucion,
        'tickets_por_tecnico': tickets_por_tecnico,
    }
    return render(request, 'tickets/informes.html', context)

