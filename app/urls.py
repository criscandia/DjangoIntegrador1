from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('nueva-remera/', views.remera, name='nueva_remera'),
    path('listar-remeras/', views.listar_remeras, name='listar_remeras'),
    path('remera/<int:id>/', views.detalles_remera, name='detalles_remera'),
    path('remera/editar/<int:id>/', views.editar_remera, name='editar_remera')
    
]