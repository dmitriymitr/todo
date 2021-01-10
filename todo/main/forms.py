from main.models import List
from django import forms


class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('name', 'user')
