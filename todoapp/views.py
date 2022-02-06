from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import *


def create(request):
    data_list = TODOModel.objects.all().order_by("-id")
    if request.method == 'POST':
        form = TODOForm(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request, "index.html", {"data": data_list, "form": TODOForm})


def delete(request, id):
    try:
        delete_data = TODOModel.objects.get(id=id)
        delete_data.delete()
        return redirect('/')
    except:
        return redirect('/')


def update(request, id):
    data_list = TODOModel.objects.all().order_by("-id")
    obj = get_object_or_404(TODOModel, id=id)
    form = TODOForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'index.html', {"data": data_list, "form": form})
