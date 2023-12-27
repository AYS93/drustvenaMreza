import random
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from django.shortcuts import render, redirect

from .forme import ObjavaForma
from .models import Objava

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def pocetni_view(request, *args, **kwargs):
    return render(request, "stranice/pocetna.html", context={}, status=200)

def objava_kreiraj_view(request, *args, **kwargs):
    forma = ObjavaForma(request.POST or None)
    next_url = request.POST.get("next") or None
    if forma.is_valid():
        obj = forma.save(commit=False)
        obj.save()
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return JsonResponse(obj.serialize(), status=201) # 201 == created items
        if next_url != None and url_has_allowed_host_and_scheme(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        forma = ObjavaForma()
    return render(request, 'komponente/forme.html', context={"forma": forma})

def objava_lista_view(request, *args, **kwargs):
    QuerySet = Objava.objects.all()
    lista_objava = [x.serialize() for x in QuerySet]
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