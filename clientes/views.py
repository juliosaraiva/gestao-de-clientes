from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Person
from .forms import PersonForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PersonList(ListView):
    model = Person


class PersonDetail(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio']
    success_url = reverse_lazy('person-list')


class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio']
    success_url = reverse_lazy('person-list')


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('person-list')


@login_required
def persons_list(request):
    persons = Person.objects.all()
    data = {'persons': persons}
    return render(request, 'person.html', data)


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    data = {'form': form}
    return render(request, 'person_form.html', data)


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    data = {'form': form}
    return render(request, 'person_form.html', data)


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == 'POST':
        person.delete()
        return redirect('persons_list')
    data = {'person': person}
    return render(request, 'person_delete_confirm.html', data)