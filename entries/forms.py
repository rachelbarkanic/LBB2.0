from django import forms
from entries.models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = {}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        