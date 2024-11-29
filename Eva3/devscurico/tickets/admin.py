from django.contrib import admin
from .models import Cliente, Ticket, Comentario

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    search_fields = ('nombre', 'email')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'estado', 'prioridad', 'tecnico_asignado', 'fecha_creacion')
    list_filter = ('estado', 'prioridad', 'tecnico_asignado')
    search_fields = ('cliente__nombre', 'descripcion')
    date_hierarchy = 'fecha_creacion'

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'autor', 'fecha')
    list_filter = ('autor', 'fecha')
    search_fields = ('ticket__id', 'autor__username', 'contenido')



# Register your models here.
