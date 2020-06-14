from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [

    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),

    path('lista-empleados/',
         views.ListAllEmpleados.as_view(),
         name='all_empleados'
    ),

    path('lista-empleados-admin/',
         views.ListaEmpleadosAdmin.as_view(),
         name='empleados_admin'
    ),


    path('lista-by-area/<shorname>/',
         views.ListByAreaEmpleado.as_view(),
         name='empleados_area'
         ),



    path('buscar-empleado/',
         views.ListEmpleadosByKeword.as_view()),


    path('listar-habilidades-empleado/<id>',
         views.ListaHabilidadesEmpleado.as_view()
         ),

    path(
         'ver-empleado/<pk>',
         views.EmpleadoDetailView.as_view(),
         name='empleado_detail'
         ),


    path('add-empleado/',
         views.EmpleadoCreateView.as_view(),
         name="empleado_add"
         ),

    path(
        'success/',
         views.SuccessView.as_view(),
        name='correcto'
    ),

    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),

    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    ),
]
