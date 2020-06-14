from django.db import models
from applications.departamento.models import Departamento
from django_ckeditor_5.fields import CKEditor5Field


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidades', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleado'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


# Create your models here.
class Empleado(models.Model):
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTROS'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombres Completos', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    avatar = models.ImageField(upload_to='empleado', blank=True, null= True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = CKEditor5Field('Text', config_name='extends')

    class Meta:
        verbose_name = 'Mis Empleados '
        verbose_name_plural = 'Empleados de la Empresa'
        ordering = ['first_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name



