from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .models import Aluno
from .forms import AlunoForm

# Create your views here.
def index(request):

    alunos = Aluno.objects.all()

    context = {
        'alunos': alunos,
    }

    return render(request, 'index.html', context)

def editar(request, pk):

    aluno = Aluno.objects.get(pk=pk)

    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
           question = AlunoForm()
           question.save()
           return HttpResponseRedirect(reverse('index'))

    context = {
        'aluno': aluno,
    }

    return render(request, 'editar.html', context)

def cadastro(request):

    if request.method == "GET":
        form = AlunoForm()
        return render(request, "cadastro.html", {'form': form})


    else:
        form = AlunoForm()
        if form.is_valid():
            cliente = form.save()
            form = AlunoForm()
            return HttpResponse(reverse('index'))
    
    return render(request, "cadastro.html", {'form': form})

