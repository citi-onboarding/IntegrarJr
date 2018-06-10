from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from django.core.mail import send_mail

# Create your views here.
def index(request):
    
    # cuida dos dados vindos do form caso acionado
    
    if request.method == 'POST':
        # pega os dados do form e guar em sua variável
        
        form = Contato(request.POST)
        # verifica se o form é válido
        
        if form.is_valid():
            # coloca cada dado em sua devida variável
            name = form.cleaned_data['']
            phone = form.cleaned_data['']
            email = form.cleaned_data['']
            subject = form.cleaned_data['']
            meet = form.cleaned_data['']
            message = form.cleaned_data['']

            # Gera o corpo do Email como uma string
            entiremail = ''.format(nameContato, emailContato, phoneContato, subjectContato, messageContato, meetContato)   

            send_mail(
                subject,    # Assunto do email
                entiremail,  # Corpo do email
                '',   # aqui irá o email de envio
                [''], #aqui irá o email de destino
                
            )

    # Se a página foi acessada diretamente pelo link, o form criado é em branco
    else:
        form = Contato()

    return render(request, 'index.html', {'form': form})