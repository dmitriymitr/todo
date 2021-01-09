from django.urls import path
from todo_item.views import todo_view

app_name = 'item'

urlpatterns = [
    path('<int:pk>', todo_view, name='item'),
    path('create/', todo_view, name='create'),
    path('delete/', todo_view),
    path('edit/<int:pk>', todo_view),
]
