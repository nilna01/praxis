from django.http import request
from django.shortcuts import redirect, render
from . import models

# Create your views here.
def index (request) :
    # if request.POST :
    #     models.Task.objects.create(item=request.POST['item'])
    #     return redirect('/')

    data = models.Task.objects.all()
    print (data)
    return render(request, 'index.html', {
    'data': data,
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
            jenismakanan=request.POST['jenismakanan'],
            jumlahmakanan=request.POST['jumlahmakanan'],
            minuman=request.POST['minuman'],
            jenisminuman=request.POST['jenisminuman'],
            jumlahminuman=request.POST['jumlahminuman'],
            harga=request.POST['harga'])

        return redirect('/')
    data=models.Task.objects.all()
    return render (request, 'tambah.html', {
        'data': data,})

def update (request,id):
    if request.POST:
        models.Task.objects.filter(pk=id). update(
            makanan=request.POST['makanan'],
            jenismakanan=request.POST['jenismakanan'],
            jumlahmakanan=request.POST['jumlahmakanan'],
            minuman=request.POST['minuman'],
            jenisminuman=request.POST['jenisminuman'],
            jumlahminuman=request.POST['jumlahminuman'],
            harga=request.POST['harga'])
            
        return redirect('/')
    data=models.Task.objects.all()
    return render (request, 'update.html', {
        'data': data,})

