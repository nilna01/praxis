from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from . import models


# Create your views here.

def index(request):
    if request.POST:
        models.Task.objects.create(item=request.POST['item'])
        return redirect('/')

    task = models.Task.objects.all()
    return render(request, 'index.html', {
        'data': task,
    })

def delete(req, id):
    models.task.objects.filter(pk=id).delete()

def rincian(req, id):
    models.task.objects.filter(pk=id).first()
    return redirect('/')