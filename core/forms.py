from django import forms

class Contato(forms.Form):
    comoConheceuOp=(
        ('Selecione', 'Como conheceu a Integrar?'),
        ('Redes sociais', 'Redes sociais'),
        ('Indicação', 'Indicação'),
        ('Pesquisa', 'Pesquisa'),
        ('Outros', 'Outros'),
    )

    nameContato = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    emailContato = forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phoneContato = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Telefone'}))
    subjectContato = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Assunto'}))
    messageContato = forms.CharField(label="", widget=forms.Textarea(attrs={'width':"100%", 'cols' : "30", 'rows': "5", 'placeholder': 'Mensagem'}))

    meetContato = forms.ChoiceField(label="", choices=comoConheceuOp)  
