from django.shortcuts import render, redirect, reverse
from main.models import List
from main.forms import ListForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views import generic
from copy import copy
from django.contrib.auth.mixins import LoginRequiredMixin
from settings import DIV_COUNT


@login_required(login_url=reverse_lazy('registration: login'))
def main_view(request):

    lists = List.objects.filter(
        user=request.user
    ).order_by('created')

    paginator = Paginator(lists, DIV_COUNT)
    page = request.GET.get('page', 1)
    is_paginated = len(lists) > DIV_COUNT
    page_obj = paginator.page(page)

    context = {
        'listmodel_list': page_obj.object_list,
        'user_name': request.user.username,
        'paginator': paginator,
        'is_paginated': is_paginated,
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)


class MainView(LoginRequiredMixin, generic.ListView):

    login_url = reverse_lazy('registration:login')
    model = List
    template_name = 'index.html'
    paginate_by = DIV_COUNT
    ordering = ['created', 'name']
    context_object_name = 'lists'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.user.username
        return context


@login_required(login_url=reverse_lazy('registration: login'))
def create_view(request):

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


class CreateView(LoginRequiredMixin, generic.CreateView):
    model = List
    template_name = 'new_list.html'
    form_class = ListForm
    success_url = reverse_lazy('main:main')
    login_url = reverse_lazy('registration:login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        query_dict = kwargs.get('data')

        if query_dict:
            query_dict = copy(query_dict)
            query_dict['user'] = self.request.user
            kwargs['data'] = query_dict

        return kwargs


@login_required(login_url=reverse_lazy('registration:login'))
def edit_view(request, pk):

    list_ = List.objects.get(id=pk)

    if request.method == 'POST':
        form = ListForm({
            'user': request.user,
            'name': request.POST.get('name')
        }, instance=list_)

        if form.is_valid():
            success_url = reverse('main:main')
            form.save()
            return redirect(success_url)
    else:
        form = ListForm(instance=list_)

    context = {
        'form': form,
        'pk': pk
    }
    return render(request, 'edit_list.html', context)


@login_required(login_url=reverse_lazy('registration:login'))
def delete_view(request, pk):

    List.objects.get(id=pk).delete()
    success_url = reverse('main:main')
    return redirect(success_url)
