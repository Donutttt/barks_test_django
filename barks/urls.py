from django.conf.urls import url
from django.contrib import admin

from website import views
                     
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^test$', views.test),
    url(r'^animals$', views.animals),
    url(r'^animals_data$', views.animals_data),
    url(r'^news_events$', views.news_and_events),
]

from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
