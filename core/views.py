from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import Contato
from django.core.mail import send_mail

# Create your views here.
def index(request):
    # cuida dos dados vindos do form caso acionado  
    if request.method == 'POST':
        # pega os dados do form e guarda em sua variável    
        form = Contato(request.POST)
        # verifica se o form é válido     
        if form.is_valid():
            # coloca cada dado em sua devida variável
            name = form.cleaned_data['nameContato']
            phone = form.cleaned_data['mailContato']
            mail = form.cleaned_data['phoneContato']
            subject = form.cleaned_data['subjectContato']
            meet = form.cleaned_data['meetContato']
            message = form.cleaned_data['messageContato']
            # Gera o corpo do Email como uma string
            entiremail = 'Nome:{}\nTelefone: {}\nEmail: {}\nComo conheceu: {}\nMensagem: {}'.format(name, mail, phone, subject, message, meet)   
            send_mail(
                subject,    # Assunto do email
                entiremail,  # Corpo do email
                'mensageiro.integrar@gmail.com',   # aqui irá o email de envio
                ['consultoria.integrarjr@gmail.com'], #aqui irá o email de destino
                fail_silently=False
            )
    # Se a página foi acessada diretamente pelo link, o form criado é em branco
    else:
        form = Contato()
    return render(request, 'index.html', {'form': form})