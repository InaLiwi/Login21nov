from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    # path(palabra_del_SLACH, FUNCION_DE_views, NOMBRE_PARA_LLAMAR_DESDE_EL_html)    
    path('', views.inicio, name='inicio'),

    path('usuarios', views.usuarios, name='usuarios'),
    path('crear_usuario', views.crear_usuario, name='crear_usuario'),
    path('editar_usuario/<int:usuario_id>', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<str:usuario_id>', views.eliminar_usuario, name='eliminar_usuario'),

    path('tickets', views.tickets, name='tickets'),
    path('crear_ticket', views.crear_ticket, name='crear_ticket'),
    path('editar_ticket/<str:ticket_id>', views.editar_ticket, name='editar_ticket'),
    path('eliminar_ticket/<str:ticket_id>', views.eliminar_ticket, name='eliminar_ticket'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
