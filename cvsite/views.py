from django.shortcuts import render
from .models import cvelement


def cvsite(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/homepage.html', {'cvelements': cvelements})

def contatti(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/contatti.html', {'cvelements': cvelements})

def curriculum(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/curriculum.html', {'cvelements': cvelements})

def index(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/index.html', {'cvelements': cvelements})


