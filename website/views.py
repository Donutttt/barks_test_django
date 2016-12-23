from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from django.forms import ModelForm
from website.models import Animal, NewsItem, Event

import json

def index(request):
    return render(request, 'website/index.html', {})



def animals_data(request):
    animals = Animal.objects.filter().values('name', 'description', 'age', 'type', 'image')

    dataDict = {
        "animals": animals,
    }

    return JsonResponse(list(animals), safe=False)


def animals(request):
    return render(request, 'website/animals.html', {})


def news_and_events(request):

    from django.core.paginator import Paginator

    requestedPage = int(request.GET.get('p', '1'))

    news = Paginator(NewsItem.objects.all().order_by('-record_input'), 2)
    events = Paginator(Event.objects.all().order_by('-event_start'), 5)

    dataDict = {
        "requestedPage": requestedPage,
        "news": news.page(requestedPage),
        "newsPagesRange": news.page_range,
        "events": events,
    }

    return render(request, 'website/news_and_events.html', dataDict)


def test(request):
    return HttpResponse("test reached return")
