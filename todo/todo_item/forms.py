from todo_item.models import ItemModel
from django import forms


class ItemForm(forms.ModelForm):

    expare_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = ItemModel
        fields = ('name', 'list_model', 'expare_date')
