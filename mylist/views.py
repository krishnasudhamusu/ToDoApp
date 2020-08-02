from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Todo


# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    context = {
        'todo_items': todo_items
    }
    return render(request, 'mylist/index.html', context)


def add_todo(request):
    added_date = timezone.now()
    content = request.POST["content"]
    Todo.objects.create(added_date=added_date, text=content)
    return HttpResponseRedirect('/')


def delete_todo(request , todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')


