from django import forms

class Contato(forms.Form):
    comoConheceuOp=()

    nameContato = forms.CharField()
    emailContato = forms.EmailField()
    phoneContato = forms.CharField()
    subjectContato = forms.CharField()
    messageContato = forms.CharField()
    meetContato = forms.ChoiceField()  
