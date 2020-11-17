from django.shortcuts import render
from forms.forms import ImageForm
from forms.models import Image


def image(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img = form.instance
            return render(request, 'forms.html', {'form': form,'img': img})
    else:
        form = ImageForm()
    return render(request, 'forms.html', {'form': form, })
