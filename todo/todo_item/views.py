from django.shortcuts import render
from todo_item.models import ItemModel


def todo_view(request):

    lists = ItemModel.objects.filter(
        user=request.user
    )

    context = {
        'lists': lists
    }

    return render(request, 'list.html', context)
