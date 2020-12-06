from django.shortcuts import render

todo_data = {
    'do': [
        {'name': 'Купить шариков', 'is_done': False},
        {'name': 'Заказать торт', 'is_done': False, 'date': '05.06.2019'},
        {'name': 'Разослать приглашения', 'is_done': False}
    ],
    'user_name': 'Admin',
}


def todo_view(request):
    context = todo_data
    return render(request, 'list.html', context)


