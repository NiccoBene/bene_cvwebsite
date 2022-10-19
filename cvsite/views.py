from django.shortcuts import render
from .models import cvelement
from django.http import Http404
from django.shortcuts import render
import mimetypes
import os
from django.http.response import HttpResponse


def cvsite(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/homepage.html', {'cvelements': cvelements})

def detail(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/detail.html', {'cvelements': cvelements})





def detail(request, cvelement_id):

    try:
        element = cvelement.objects.get(pk=cvelement_id)

    except cvelement.DoesNotExist:
        raise Http404("CV element does not exist")
    return render(request, 'cvsite/detail.html', {'element': element})


def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		# Modifica filename con il nome e l'estensione del file che vuoi far scaricare	
    filename = 'niccobenecv.pdf'
    filepath = BASE_DIR + '/download/' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
