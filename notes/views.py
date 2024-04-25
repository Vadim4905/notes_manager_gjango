from django.urls import reverse_lazy
from . import models
from django.views.generic import ListView,DetailView,CreateView
from . import forms

# Create your views here.
class NoteListView(ListView):
    model= models.Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    
class  NoteDetailView(DetailView):
    model = models.Note 
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'
    
class NoteCreateView(CreateView):
    template_name = 'notes/note_form.html'
    form_class = forms.NoteForm
    success_url = reverse_lazy('note-list')
      
