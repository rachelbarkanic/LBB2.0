from django import forms
from entries.models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = {'beer_name', 'brewery_name', 'beer_style', 'beer_pic', 'rating', 'content'}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['beer_name'].widget.attrs['placeholder'] = 'Beer Name'
        self.fields['brewery_name'].widget.attrs['placeholder'] = 'Brewery Name'
        self.fields['beer_style'].widget.attrs['placeholder'] = 'Beer Style'
        self.fields['beer_pic'].widget.attrs['placeholder'] = 'Beer Photo'
        self.fields['rating'].widget.attrs['placeholder'] = 'Rating'
        self.fields['content'].widget.attrs['placeholder'] = 'Notes'

        