from forms.models import Image
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')
def account(request):
    return render(request, 'account.html')

def index(request):
    names = Image.objects.all().order_by("-date_added")
    return render(request, 'home.html', {"names":names})
