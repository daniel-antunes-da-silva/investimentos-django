from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required # para a pessoa precisar fazer login

# Create your views here.

'''
def pagina_inicial(request):
    return HttpResponse('Pronto para investir!')'''


'''def contato(request):
    return HttpResponse('Para dúvidas, enviar um e-mail para: contato@suporte.com')


def minha_historia(request):
    pessoa = {
        'nome': 'Jeff',
        'idade': '28',
        'hobby': 'Games'
    }
    return render(request, 'investimentos/minha_historia.html', pessoa)
'''


'''def novo_investimento(request):
    return render(request, 'investimentos/novo_investimento.html')'''


'''def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('TipoInvestimento')
    }
    return render(request, 'investimentos/investimento_registrado.html', investimento)'''


def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()  # retorna todos os registros (objetos) que estão no BD
    }
    return render(request, 'investimentos/investimentos.html', context=dados)


def detalhes(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', dados)


@login_required
def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()  # se for válido, vai salvar no banco de dados.
        return redirect('investimentos')  # redireciona o usuário para a url inicial,
        # que foi nomeada como investimentos.
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)


@login_required
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    # novo_investimento/1 --> GET | Por isso, devemos tratar essa situação:
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)  # passamos o dado que foi pesquisado dentro do BD.
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    # Caso a requisição seja POST:
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')


@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    # Se não for um POST, estaremos lidando com um GET, que é o padrão.
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})
