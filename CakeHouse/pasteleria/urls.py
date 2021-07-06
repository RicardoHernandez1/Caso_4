from django.urls import path

from . import views

app_name = 'pasteleria'
urlpatterns = [
    path('', views.index, name='index'),
    path('frm_agregar_usuario', views.frm_agregar_usuario, name='frm_agregar_usuario'),
    path('registrar_usuario', views.registrar_usuario, name='registrar_usuario'),
    path('mendocinos', views.mendocinos, name='mendocinos'),
    path('torta_sanjorge', views.torta_sanjorge, name='torta_sanjorge'),
    path('caja_bombones', views.caja_bombones, name='caja_bombones'),
    path('login', views.login, name='login'),
    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),

]

