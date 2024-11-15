from django.shortcuts import render,redirect
from .models import Empleado
# Create your views here.

def inicio_vista(request):
    elempleado=Empleado.objects.all()

    return render(request,"gestionarEmpleado.html",{"elempleado":elempleado})


def registrarEmpleado(request):
    id_empleado =request.POST["txtid_empleado"]
    nombre =request.POST["textnombre"]
    apellido  =request.POST["textapellido"]
    horario  =request.POST["datehorario"] 
    salario  =request.POST["numsalario"]
    telefono  =request.POST["txttelefono"]
    guardar=Empleado.objects.create(id_empleado=id_empleado,nombre=nombre,apellido=apellido,
    horario=horario,salario=salario,telefono=telefono)
    return redirect("/")

def seleccionarEmpleado(request,id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    return render(request,"editarEmpleado.html",{"elempleado":empleado})

def editarEmpleado(request):
    id_empleado =request.POST["txtid_empleado"]
    nombre =request.POST["textnombre"]
    apellido  =request.POST["textapellido"]
    horario  =request.POST["datehorario"] 
    salario  =request.POST["numsalario"]
    telefono  =request.POST["txttelefono"]
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre=nombre
    empleado.apellido=apellido
    empleado.horario=horario
    empleado.salario=salario
    empleado.telefono=telefono
    empleado.save()
    return redirect("/")

def borrarEmpleado(request,id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("/")