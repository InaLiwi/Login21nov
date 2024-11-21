from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    # path(palabra_del_SLACH, FUNCION_DE_views, NOMBRE_PARA_LLAMAR_DESDE_EL_html)    
    path('', views.home, name='home'),

    path('usuarios', views.usuarios, name='usuarios'),
    path('crear_usuario', views.crear_usuario, name='crear_usuario'),
    path('editar_usuario/<str:usuario_nombre_usuario>', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<str:usuario_nombre_usuario>', views.eliminar_usuario, name='eliminar_usuario'),

    path('tickets', views.tickets, name='tickets'),
    path('tickets/crear', views.crear_ticket, name='crear_ticket'),
    path('editar_ticket/<str:ticket_id>', views.editar_ticket, name='editar_ticket'),
    path('eliminar_ticket/<str:ticket_id>', views.eliminar_ticket, name='eliminar_ticket'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
