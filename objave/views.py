import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Objava
# Create your views here.
def pocetni_view(request, *args, **kwargs):
    return render(request, "stranice/pocetna.html", context={}, status=200)

def objava_lista_view(request, *args, **kwargs):
    QuerySet = Objava.objects.all()
    lista_objava = [{"id": x.id, "sadrzaj": x.sadrzaj, "svidjanja": random.randint(0, 131)} for x in QuerySet]
    data = {
        "response": lista_objava
    }
    return JsonResponse(data)

def objava_detaljni_view(request, objava_id, *args, **kwargs):
    data = {
        "id": objava_id
    }
    status = 200
    try:
        obj = Objava.objects.get(id=objava_id)
        data['sadrzaj'] = obj.sadrzaj
    except:
        data['poruka'] = "Ups! Nije pronadjeno."
        status = 404
    
    return JsonResponse(data, status=status)