from django.shortcuts import render
from .models import cvelement
from django.http import Http404
from django.shortcuts import render



def cvsite(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/homepage.html', {'cvelements': cvelements})

def detail(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/detail.html', {'cvelements': cvelements})

def curriculum(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/curriculum.html', {'cvelements': cvelements})

def index(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/index.html', {'cvelements': cvelements})

def detail(request, cvelement_id):

    try:
        element = cvelement.objects.get(pk=cvelement_id)

    except cvelement.DoesNotExist:
        raise Http404("CV element does not exist")
    return render(request, 'cvsite/detail.html', {'element': element})
