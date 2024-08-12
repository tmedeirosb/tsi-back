from django import forms
from .models import Agenda

# class InsereAgendaForm(forms.Form):
#     nome = forms.CharField(
#         max_length=100,
#         required=True
#     )
#     telefone = forms.IntegerField(
#         required=True
#     )

class InsereAgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['nome', 'telefone']