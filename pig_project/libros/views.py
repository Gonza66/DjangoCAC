from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
#def saludon(request,nombre):

#    return HttpResponse(f"HOLA {nombre}")

def saludo(request,nombre=''):
    return HttpResponse(f"HOLA {nombre}")


def despedida(request):
    return HttpResponse("ADIOS")

def nada(request):
    return HttpResponse("""<h1>llegada al servidor</h1>
    <br>
    <h3> linea h3 </h3>""")

def saludo_serio(request,nombre):
    return HttpResponse(f"Cómo está usted Sr. {nombre}")

def vacio(request):
    return HttpResponse('no se saluda a nadie')

"""def index(request):
    template=loader.get_template('index.html')
    libro='La guerra y la paz'
    autor='Leon Tolstoi'
    contexto={'libro': libro, 'autor': autor}
    return HttpResponse(template.render(contexto, request))"""

def index(request):
    libro='La guerra y la paz'
    autor='Leon Tolstoi'
    diccionario={'libro': libro, 'autor': autor}
    #return render(request,'index.html',{'libro': libro, 'autor': autor})
    return render(request,'index.html',diccionario)
