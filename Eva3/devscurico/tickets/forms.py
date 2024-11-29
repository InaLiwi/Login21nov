from django import forms
from .models import Ticket, Comentario

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['cliente', 'descripcion', 'prioridad', 'estado', 'tecnico_asignado']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']

