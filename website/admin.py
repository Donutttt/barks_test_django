from django.contrib import admin
from .models import Animal, NewsItem, Event, Contact, AnimalContact

admin.site.register(Animal)
admin.site.register(NewsItem)
admin.site.register(Event)
admin.site.register(Contact)
admin.site.register(AnimalContact)
