from main.models import List
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS


class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('name', 'user')
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Имя уже существует",
            }
        }
