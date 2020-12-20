from django.urls import path
from todo_item.views import todo_view

app_name = 'item'

urlpatterns = [
    path('', todo_view),
    path('create/', todo_view),
    path('delete/', todo_view),
    path('edit/', todo_view),
]
