from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Agenda
from .forms import InsereAgendaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    contatos = Agenda.objects.all()

    resultado = 10 + 10
    contexto = {
        'resultado': resultado,
        'nome': 'João',
        'contatos': contatos
    }
    return render(request, 'home.html', contexto)
    #return HttpResponse('Hello, World!')

def teste(request):
    return HttpResponse('Teste')

def agenda(request):
    #retornar a lista de contatos
    contatos = Agenda.objects.all()

    saida = '<table border=1>'

    for contato in contatos:
        nome = contato.nome
        telefone = contato.telefone
        saida += f'<tr><td>{nome}</td><td>{telefone}</td></tr>'

    saida += '</table>'

    return HttpResponse(saida)

# def inserir(request):
#     form = InsereAgendaForm() 

#     pagina = '<html><head><title>Inserir contato</title></head><body>'
#     pagina += '<h1>Inserir contato</h1>'
#     pagina += '<form method="POST" action="/ok/">'
#     pagina += str(form)
#     pagina += '<button name="inserir">Inserir dados</button>'
#     pagina += '</form></body></html>'

#     #retornar o formulário de inserção
#     return HttpResponse(pagina)

def inserir(request):
    form = InsereAgendaForm()
    return render(request, 'form_inserir.html', {'form': form})

def ok(request):
    #return HttpResponse('Ok')
    if request.method == 'POST':
        form = InsereAgendaForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse('Contato inserido com sucesso!')
            return redirect('home')
        else:
            return HttpResponse('Formulário inválido')
    else:
        return HttpResponse('Método inválido')
    
class AgendaListView(ListView):
    model = Agenda
    template_name = 'home.html'
    context_object_name = 'contatos'

class AgendaCreateView(CreateView):
    model = Agenda
    fields = ['nome', 'telefone']
    template_name = 'form_inserir.html'
    success_url = '/listar/'

class Agenda2CreateView(CreateView):
    model = Agenda
    form_class = InsereAgendaForm
    template_name = 'form_inserir.html'
    success_url = reverse_lazy('listar')

class AgendaUpdateView(UpdateView):
    model = Agenda
    fields = '__all__'
    template_name = 'form_atualizar.html'
    success_url = '/listar/'

class AgendaDeleteView(DeleteView):
    model = Agenda
    template_name = 'confirmar_delete.html'
    success_url = '/listar/'
    
