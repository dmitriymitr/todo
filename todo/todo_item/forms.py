from todo_item.models import ItemModel
from django import forms
from django.core.exceptions import  NON_FIELD_ERRORS


class ItemForm(forms.ModelForm):

    expare_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = ItemModel
        fields = ('name', 'list_model', 'expare_date')
        error = {
            NON_FIELD_ERRORS: {
                'unique_together': "Такое дело уже существует"
            }
        }
