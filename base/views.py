from django.shortcuts import render

def home(request):
    return render(request,'base/index.html',{})

def left_sidebar(request):
    return render(request,'base/left_sidebar.html',{})


def hija1(request):
    return render(request,'base/hija1.html',{})

def perfil(request):
    return render(request,'base/perfil.html',{})

def plantilla(request):
    datos = {
        'lista': ['primero','segundo','tercero'],
        'nombre': 'Gael',
        'apellido': "Fort"
    }
    return render(request, 'base/plantilla.html', datos)