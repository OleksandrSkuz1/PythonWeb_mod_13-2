from django.forms import ModelForm, CharField, ImageField

from .models import Author

class AuthorForm(ModelForm):
    description = CharField(max_length=100, min_length=5)


    class Meta:
        model = Author
        fields = ['description, path']

