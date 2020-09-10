from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import CreateNewList
from .models import ToDoList
from django.utils.text import slugify

# Create your views here.


def matheus(response):
    template_name = 'main/matheus.html'
    return render(response, template_name, {})


def home(response):
    template_name = 'main/home.html'
    return render(response, template_name, {})


@login_required
def create(response):
    template_name = 'main/create.html'
    if response.method == "POST":
        form = CreateNewList(response.POST)
        # Salvando nova lista de itens
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
            response.user.lists.add(t)
        return redirect(f'/list_view/{t.id}-{slugify(t.name)}/')

    else:
        form = CreateNewList()
    return render(response, template_name, {"form": form})


@login_required
def list_view(response, id, name):
    lst = ToDoList.objects.get(id=id)
    print(lst)

    if lst not in response.user.lists.all():
        return redirect('register:dashboard')
    else:
        template_name = 'main/list.html'
        if response.method == "POST":
            # Printar na tela o POST retornado
            print(response.POST)
            if response.POST.get("save"):
                for item in lst.itens.all():
                    if response.POST.get('c' + str(item.id)) == 'clicked':
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("newItemName")
                if len(txt) > 2:
                    lst.itens.create(text=txt, complete=False)
                else:
                    print(f'invalid')

        return render(response, template_name, {"lst": lst})