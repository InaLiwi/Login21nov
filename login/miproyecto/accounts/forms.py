from django import forms

from .models import Usuario, Ticket

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            #'usuario_fecha': forms.DateInput(attrs={'type': 'date'}),
            #'usuario_hora': forms.TimeInput(attrs={'type': 'time'}),  #cambia el campo fecha a date.
            #'usuario_duracion': forms.NumberInput()
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        widgets = {
            #'ticket_capacidad': forms.NumberInput(attrs={'type': 'number'}),
            'ticket_fecha': forms.DateInput(attrs={'type': 'date'}),
        }
