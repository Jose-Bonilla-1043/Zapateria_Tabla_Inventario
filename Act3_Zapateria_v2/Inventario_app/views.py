from django.shortcuts import render,redirect
from .models import Inventario
# Create your views here.

def inicio_vista(request):
    elinventario=Inventario.objects.all()

    return render(request,"gestionarInventario.html",{"elinventario":elinventario})


def registrarInventario(request):
    id_inventario =request.POST["txtid_inventario"]
    cantidad_actual =request.POST["numcantidad_actual"]
    cantidad_minima  =request.POST["numcantidad_minima"]
    fecha_actualizacion  =request.POST["datefecha_actual"] 
    ubicacion  =request.POST["txtubicacion"]
    historial  =request.POST["txthistorial"]
    guardar=Inventario.objects.create(id_inventario=id_inventario,cantidad_actual=cantidad_actual,cantidad_minima=cantidad_minima,
    fecha_actualizacion=fecha_actualizacion,ubicacion=ubicacion,historial=historial)
    return redirect("/")

def seleccionarInventario(request,id_inventario):
    inventario=Inventario.objects.get(id_inventario=id_inventario)
    return render(request,"editarInventario.html",{"elinventario":inventario})

def editarInventario(request):
    id_inventario =request.POST["txtid_inventario"]
    cantidad_actual =request.POST["numcantidad_actual"]
    cantidad_minima  =request.POST["numcantidad_minima"]
    fecha_actualizacion  =request.POST["datefecha_actual"] 
    ubicacion  =request.POST["txtubicacion"]
    historial  =request.POST["txthistorial"]
    inventario=Inventario.objects.get(id_inventario=id_inventario)
    inventario.cantidad_actual=cantidad_actual
    inventario.cantidad_minima=cantidad_minima
    inventario.fecha_actualizacion=fecha_actualizacion
    inventario.ubicacion=ubicacion
    inventario.historial=historial
    inventario.save()
    return redirect("/")

def borrarInventario(request,id_inventario):
    inventario=Inventario.objects.get(id_inventario=id_inventario)
    inventario.delete()
    return redirect("/")