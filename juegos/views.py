from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego
from .forms import JuegoForm

def lista_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'juegos/lista.html', {'juegos': juegos})

def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_juegos')
    else:
        form = JuegoForm()
    return render(request, 'juegos/formulario.html', {'form': form})

def editar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    if request.method == 'POST':
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('lista_juegos')
    else:
        form = JuegoForm(instance=juego)
    return render(request, 'juegos/formulario.html', {'form': form})

def eliminar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    if request.method == 'POST':
        juego.delete()
        return redirect('lista_juegos')
    return render(request, 'juegos/eliminar.html', {'juego': juego})
