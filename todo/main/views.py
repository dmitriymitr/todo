from django.shortcuts import render, redirect, reverse
from main.models import List
from main.forms import ListForm


def main_view(request):
    lists = List.objects.filter(user=request.user)
    context = {
        'lists': lists,
        'user_name': request.user.username,
    }
    return render(request, 'index.html', context)


def create_view(request):
    form = ListForm()
    if request.method == 'POST':
        form = ListForm({
            'user': request.user,
            'name': request.POST.get('name')
        })
        if form.is_valid():
            success_url = reverse('main:main')
            form.save()
            return redirect(success_url)
    return render(request, 'new_list.html', {'form': form})
