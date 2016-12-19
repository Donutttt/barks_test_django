from django.conf.urls import url
from django.contrib import admin

from website import views
                     
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^test$', views.test),
    url(r'^animals_data$', views.animals_data),
]