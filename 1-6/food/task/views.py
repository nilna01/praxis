from django.http import request
from django.shortcuts import redirect, render
from . import models

# Create your views here.
def index (request) :
    # if request.POST :
    #     models.Task.objects.create(item=request.POST['item'])
    #     return redirect('/')

    tasks = models.Task.objects.all()
    return render(request, 'index.html', {
    'data' : tasks,
    }) 
def delete(request, id) :
    models.Task.objects.filter(pk=id).delete()
    return redirect('/')

def rincian(request, id) :
    tasks=models.Task.objects.filter(pk=id).first()
    return render(request, 'detail.html', {
        'data' : tasks,
    })  

def tambah(request):
    if request.POST:
        models.Task.objects.create(
            makanan=request.POST['makanan'],
            minuman=request.POST['minuman'],
            harga=request.POST['harga'],
            jumlah=request.POST['jumlah'])

        return redirect('/')
    data=models.Task.objects.all()
    return render (request, 'tambah.html', {
        'data': data,})

def update (request,id):
    if request.POST:
        models.Task.objects.filter(pk=id). update(
            makanan=request.POST['makanan'],
            minuman=request.POST['minuman'],
            harga=request.POST['harga'],
            jumlah=request.POST['jumlah'])
            
        return redirect('/')
    data=models.Task.objects.all()
    return render (request, 'update.html', {
        'data': data,})

