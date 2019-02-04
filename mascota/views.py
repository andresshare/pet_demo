from django.shortcuts import render, redirect

from mascota.forms import Mascota_form


def index (request):
    return render(request, 'mascota/index.html')


def mascota_view(request):
    if request.method == 'POST':
        form = Mascota_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:index')

    else:

        form = Mascota_form()

    return render(request, 'mascota/mascota_form.html', {'form': form})
