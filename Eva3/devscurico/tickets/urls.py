from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('tickets/', views.lista_tickets, name='lista_tickets'),
    path('ticket/<int:ticket_id>/', views.detalle_ticket, name='detalle_ticket'),
    path('crear/', views.crear_ticket, name='crear_ticket'),
    path('actualizar/<int:ticket_id>/', views.actualizar_ticket, name='actualizar_ticket'),
    path('eliminar/<int:ticket_id>/', views.eliminar_ticket, name='eliminar_ticket'),
    path('informes/', views.informes, name='informes'),
]

