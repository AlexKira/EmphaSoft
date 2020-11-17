from django import forms
from forms.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('uname','age',"gender","about_me","image",)
