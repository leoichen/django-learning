from django import forms
from django.core.exceptions import ValidationError
from .models import Notes
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.TextInput(attrs={'class': 'form-control my-5'}),
        }
        labels = {
            'title': 'Title',
            'text': 'Your Thoughts'
        }

    
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('Need Django in the note')
        
        return title