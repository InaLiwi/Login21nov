import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devscurico.settings")
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from tickets.models import Ticket, Comentario

def create_groups():
    # Crear grupo de Técnicos
    tecnicos_group, created = Group.objects.get_or_create(name='Técnicos')
    
    # Permisos para Técnicos
    ticket_content_type = ContentType.objects.get_for_model(Ticket)
    comentario_content_type = ContentType.objects.get_for_model(Comentario)
    
    tecnicos_permissions = [
        Permission.objects.get(content_type=ticket_content_type, codename='view_ticket'),
        Permission.objects.get(content_type=ticket_content_type, codename='change_ticket'),
        Permission.objects.get(content_type=comentario_content_type, codename='add_comentario'),
        Permission.objects.get(content_type=comentario_content_type, codename='view_comentario'),
    ]
    
    tecnicos_group.permissions.set(tecnicos_permissions)
    
    # Crear grupo de Administradores
    admin_group, created = Group.objects.get_or_create(name='Administradores')
    
    # Permisos para Administradores (todos los permisos)
    admin_permissions = Permission.objects.all()
    admin_group.permissions.set(admin_permissions)
    
    print("Grupos y permisos creados exitosamente.")

if __name__ == '__main__':
    create_groups()

