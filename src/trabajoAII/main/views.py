from _datetime import date

from django.shortcuts import render

from main.models import Album
from main.populate import populateDB
from main.forms import BuscarPorTituloForm, BuscarPorFechaForm

def populate(request):
    populateDB()
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def mostrar_album(request):
    albums = Album.objects.all()
    return render(request, 'mostrar_album.html', {'albums':albums})
    
def album_mas_vendido(request):
    albums = Album.objects.all().order_by('-ventas')[:3]
    return render(request, 'album_mas_vendido.html', {'albums':albums})

def diferencia(fecha1, fecha2):
    return (fecha2 - fecha1).days

def album_preorder(request):
    albums = Album.objects.all()
    alb = []
    for a in albums:
        fecha = a.fecha
        hoy = date.today()
        result = diferencia(fecha, hoy)
        if result < 0:
            alb.append(a)
    return render(request, 'album_preorder.html', {'alb':alb})

def buscar_por_titulo(request):
    formulario = BuscarPorTituloForm(request.POST)
    albums = None
    
    if request.method=='POST':
        formulario = BuscarPorTituloForm(request.POST)
        
        if formulario.is_valid():
            albums = Album.objects.filter(titulo__contains = formulario.cleaned_data['titulo'])
            
    return render(request, 'buscar_por_titulo.html', {'formulario':formulario, 'albums':albums})

def formatear_fecha(f):
    #17-01-2020 en el form
    #2020-01-17 tiene q estar
    
    partes = f.split("-")
    fecha = "-".join(reversed(partes))
    return fecha

def buscar_por_fecha(request):
    formulario = BuscarPorFechaForm(request.POST)
    albums = []
    all = Album.objects.all()
    if request.method=='POST':
        formulario = BuscarPorFechaForm(request.POST)
        
        if formulario.is_valid():
            for a in all:
                fecha = a.fecha 
                form = formulario.cleaned_data['fecha']
                result = diferencia(fecha, form)
                
                if result < 0:
                    albums.append(a)
            
    return render(request, 'buscar_por_fecha.html', {'formulario':formulario, 'albums':albums})










