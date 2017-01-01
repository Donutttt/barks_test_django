from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from django.forms import ModelForm
from django.utils.html import strip_tags
from website.models import Animal, NewsItem, Event, Contact, AnimalContact
from .forms import AnimalContactForm

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

def animal_contact(request, requestedAnimalId):

    dataDict = {
        "requestedAnimalId": requestedAnimalId,        
        "method": request.method,
        "formSubmitted": False,
    }

    if request.method == 'POST':
        # when the method is post, the form has been submitted

        from django.core.mail import send_mail

        dataDict['formSubmitted'] = True
        postedForm = AnimalContactForm(request.POST)

        if postedForm.is_valid():
            cleanedData = postedForm.cleaned_data
            sentAnimalId = int(strip_tags(request.POST.get('animalId', '0'))) # extra care as not auto handled by django

            animalMatchingSentId = requestedAnimal = Animal.objects.filter(id = sentAnimalId).first()
                
            newAnimalContact = AnimalContact(
                contact_name = cleanedData['nameField'],
                contact_email = cleanedData['emailField'],
                contact_text = cleanedData['textField'],
                animal_name = animalMatchingSentId.name,
                animal_id = sentAnimalId,
            )

            newAnimalContact.save()

            send_mail(
                subject = "A message about {} from {}".format(cleanedData['nameField'], animalMatchingSentId.name),
                message = "The following message was sent: {}".format(cleanedData['textField']),
                from_email = "orr2@live.com",
                recipient_list = ["orr2@live.com"],
            )

    else:
        # just the regular page
        form = AnimalContactForm()
        dataDict['form'] = form

    return render(request, 'website/animal_contact.html', dataDict)

def test(request):
    return HttpResponse("test reached return")
