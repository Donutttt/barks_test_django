from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from django.forms import ModelForm
from website.models import Animal, NewsItem, Event, Contact

import json

def index(request):
    return render(request, 'website/index.html', {})



def animals_data(request):
    animals = Animal.objects.filter().values('name', 'description', 'age', 'type', 'image', "id")

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
        "events": events.page(1),
    }

    return render(request, 'website/news_and_events.html', dataDict)

def contacts(request):
    contacts = Contact.objects.all() 

    dataDict = {
        "contacts": contacts,
    }

    return render(request, 'website/contact.html', dataDict)

def donate(request):
    return render(request, 'website/donate.html', {})


def animal(request, animalId):
    requestedAnimal = Animal.objects.filter(id = animalId).first()

    dataDict = {
        "animalId": animalId,        
        "requestedAnimal": requestedAnimal,
    }    

    return render(request, 'website/animal.html', dataDict)

def news_item(request, newsItemId):
    requestedNewsItem = NewsItem.objects.filter(id = newsItemId).first()

    dataDict = {
        "newsItemId": newsItemId,
        "requestedNewsItem": requestedNewsItem,
    }

    return render(request, 'website/news_item.html', dataDict)

def event(request, eventId):
    requestedEventItem = Event.objects.filter(id = eventId).first() 

    dataDict = {
        "eventId": eventId,
        "eventItem": requestedEventItem,
    }

    return render(request, 'website/event.html', dataDict)

def test(request):
    return HttpResponse("test reached return")
