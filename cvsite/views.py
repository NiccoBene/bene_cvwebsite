from django.shortcuts import render
from .models import cvelement


def cvsite(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/homepage.html', {'cvelements': cvelements})

def contatti(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/contatti.html', {'cvelements': cvelements})

def progetti(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/progetti.html', {'cvelements': cvelements})


