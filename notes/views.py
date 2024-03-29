from django.shortcuts import render
from django.http import Http404
from .models import Notes
from .forms import NotesForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = "notes/notes_list.html"

class NotesListDetailView(DetailView):
    model = Notes
    context_object_name = 'note'


# Create your views here.
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk = pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
    
#     return render(request, 'notes/notes_detail.html', {'note': note})
