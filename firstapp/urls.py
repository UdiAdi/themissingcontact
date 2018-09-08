from django.conf.urls import include, url
from firstapp import views

urlpatterns = [
    url(r'^$', views.firstapp_view, name="firstapp_view"),
   ]
