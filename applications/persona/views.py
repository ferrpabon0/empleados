from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Empleado
from django.urls import reverse_lazy

#forms
from .forms import EmpleadoForm


class InicioView(TemplateView):
    template_name = 'inicio.html'



class ListAllEmpleados(ListView):
    template_name = "persona/lista-empleados.html"
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'lista_empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )

        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = "persona/lista_empleados.html"
    paginate_by = 10
    ordering = 'first_name'
    model = Empleado
    context_object_name = 'empleados'





#Lista de empleados por área con parametro URL

class ListByAreaEmpleado(ListView):
    template_name = "persona/lista-by-area.html"
    context_object_name = 'empleados'
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista


class ListEmpleadosByKeword(ListView):
    # Lista empleados por palabra clave

    template_name = 'persona/lista-by-keyword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('Holaaaaaaaaaaaaaaaaaa')
        palabra_clave = self.request.GET.get("kword",'')

        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        print('lista resultado', lista)
        return lista



class ListaHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'


    def get_queryset(self):
        #obtener un unico registro de la base de datos get

        empleado = Empleado.objects.get(id=self.kwargs['id'])
        return empleado.habilidades.all()



class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail_empleado.html'

    #Enviar un parametro diferente como empleado del mes
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)

        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = 'persona/success.html'


class EmpleadoCreateView(CreateView):

    template_name = 'persona/add.html'
    model = Empleado
    form_class = EmpleadoForm

    # fields = ('__all__') Todos los datos
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):

        empleado = form.save(commit=False)  # para no hacer 2ble guardado instancia
        empleado.fullname = empleado.first_name + '' + empleado.last_name
        empleado.save()

        return super(EmpleadoCreateView,self).form_valid(form)




class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado

    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'hoja_vida',

    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    #Utilizar post cuando queramos guardar datos antes de ser validados por form_valid

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        print('-----------METODO POST-------------')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('-----------METODO FORM VALID-------------')
        return super(EmpleadoUpdateView, self).form_valid(form)




class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')


