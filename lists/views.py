import imp
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse

# Create your views here.
from .models import Tarefa

from .forms import TarefaForm


def editar_tarefa(request,id):
    tarefa_editar = get_object_or_404(Tarefa,id=id)
    form = TarefaForm(instance=tarefa_editar)
    if request.POST:
        form= TarefaForm(request.POST,instance=tarefa_editar)
        if form.is_valid():
            form.user=request.user
            form.save()
            return redirect('todas_tarefas')
    context={
        'form':form
    }
    return render (request,'editar.html',context)
def todas_tarefas (request):
    tarefas =Tarefa.objects.all()
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('todas_tarefas')
        else:
            return HttpResponse('Bad request')
    form= TarefaForm()

    context={
        'tarefas':tarefas,
        'form':form,
    }
    return render (request,'index.html',context)
def deletar_tarefa(request,id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect ('todas_tarefas')
