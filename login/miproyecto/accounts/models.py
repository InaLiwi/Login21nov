from django.db import models

# Create your models here.
#    libro_imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagennn', null=True, blank=True)
class Usuario(models.Model):
    usuario_id = models.AutoField(max_length=11, primary_key=True)
    usuario_rol = models.CharField(max_length=50, primary_key=True, verbose_name='Especifique el rol: ')
    usuario_nombre_usuario = models.CharField(max_length=20, primary_key=True, verbose_name='Nombre usuario')
    
    def __str__(self):
        fila = "usuario: " + self.usuario_nombre + " || " + "Capacidad: " + str(self.usuario_capacidad) + " || " + "Ubicación: " + self.usuario_ubicacion
        return fila
    
    '''
    def delete(self, using=None, keep_parents=False):
        self.libro_imagen.storage.delete(self.libro_imagen.name)
        super().delete()
    '''


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_numero_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, max_length=20, verbose_name='Nombre usuario')
    ticket_fecha = models.DateField(verbose_name='Fecha')
    ticket_prioridad = models.CharField(max_length=20, verbose_name='Prioridad (Alta-Media-Baja): ')
    ticket_descripcion = models.FloatField(max_length=100, verbose_name='Descripción: ')

    def __str__(self): #En este caso, self.ticket_nombre_usuario es un objeto usuario (ya que ticket_nombre_usuario es una clave foránea). Por eso, hay que concatenarlo con str()
        fila = "ticket: " + str(self.ticket_id) + " --- " + "usuario: " + str(self.ticket_nombre_usuario.usuario_nombre) + " || "  + "Usuario: " + self.ticket_nombre_usuario  + " || "  + str(self.ticket_fecha) + " a las " + str(self.ticket_hora) + " || "  + "Duración: " + str(self.ticket_duracion) + " hora(s)"
        return fila


#python manage.py makemigrations
#nos permite crear un archivo para migrar, debemos ejecutar este comando cada vez que modifiquemos el modelo de la bd

#python manage.py migrate
#aplica las migraciones creadas, sincroniza su estructura, modificaciones etc...
    
# yoyo - 1234
    
    
    