from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse

import json

from website.models import Animal

def index(request):


    return render(request, 'website/index.html', {})


def animals_data(request):

    animals = Animal.objects.filter().values('name', 'description', 'age')

    dataDict = {
        "animals": animals,
    }


    return JsonResponse(list(animals), safe=False)





def test(request):
    
    return HttpResponse("test reached return")
