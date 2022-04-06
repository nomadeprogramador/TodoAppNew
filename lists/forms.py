from django import forms
from .models import Tarefa



class TarefaForm(forms.ModelForm):


    class Meta:
        model=Tarefa    
        widgets = {
          'conteudo': forms.Textarea(attrs={'rows':'3', 'cols':'3'}),
        }
        fields = ('__all__')
     