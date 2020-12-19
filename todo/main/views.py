from django.shortcuts import render
from main.models import List


def main_view(request):

    lists = List.objects.filter(user=request.user)

    context = {
        'lists': lists,
        'user_name': request.user.username,
    }
    return render(request, 'index.html', context)
