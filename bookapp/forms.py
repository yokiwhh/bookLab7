
from django import forms
from models import *



class BookForm(forms.ModelForm):
	
    class Meta:
        model = Book	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

