from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Ticket(models.Model):
    ESTADO_CHOICES = [
        ('AB', 'Abierto'),
        ('EP', 'En Proceso'),
        ('RE', 'Resuelto'),
        ('CE', 'Cerrado'),
    ]
    PRIORIDAD_CHOICES = [
        ('BA', 'Baja'),
        ('ME', 'Media'),
        ('AL', 'Alta'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    prioridad = models.CharField(max_length=2, choices=PRIORIDAD_CHOICES)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES, default='AB')
    tecnico_asignado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_asignacion = models.DateTimeField(null=True, blank=True)
    fecha_resolucion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Ticket {self.id} - {self.cliente.nombre}"

class Comentario(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} en Ticket {self.ticket.id}"

