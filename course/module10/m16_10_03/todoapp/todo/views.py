from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo
from .forms import TodoForm


# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = 'todo/list.html'
    form_class = TodoForm
    context_object_name = 'todo_list'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(TodoListView, self).get_queryset()
        print(queryset)
        return queryset


class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo/create.html'
    form_class = TodoForm
    success_url = reverse_lazy('main')


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo/update.html'
    fields = ('title', 'description', 'completed')
    success_url = reverse_lazy('main')


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('main')
