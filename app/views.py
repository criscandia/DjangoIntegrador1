from django.shortcuts import render, redirect, get_object_or_404

from .forms import RemerasForm
from .models import Remeras  # Import the Remeras model
# Create your views here.

def home(request, template_name='app/home.html'):
    return render(request, template_name)

def contacto(request, template_name='app/contacto.html'):
    return render(request, template_name)

def remera(request, template_name='app/nueva-remera.html'):
    if request.method == 'POST':
        form = RemerasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        pass
    else:
        form = RemerasForm()
    dato = {'form': form}
    return render(request, template_name, dato)

def editar_remera(request, id, template_name='app/editar-remera.html'):
    remera = get_object_or_404(Remeras, pk=id)
    form = RemerasForm(request.POST or None, instance=remera)
    if form.is_valid():
        form.save()
        return redirect('listar_remeras')
    dato = {'form': form}
    return render(request, template_name, dato)

def listar_remeras(request, template_name='app/listar-remeras.html'):
    remeras_list = Remeras.objects.all()
    dato = {'remeras': remeras_list}
    return render(request, template_name, dato)

def detalles_remera(request, id):
    remera = get_object_or_404(Remeras, pk=id)
    return render(request, 'app/detalles_remera.html', {'remera': remera})

