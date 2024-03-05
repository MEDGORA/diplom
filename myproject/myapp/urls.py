from django.urls import path, include
from . import views
from .views import home, about, vacansies, personal, news, for_consumers, contacts, requisites, form, successful_form

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('vacansies', vacansies, name="vacansies"),
    path('personal', personal, name="personal"),
    path('news', news, name="news"),
    path('for_consumers', for_consumers, name="for_consumers"),
    path('contacts', contacts, name="contacts"),
    path('requisites', requisites, name="requisites"),
    path('form', form, name="form"),
    path('successful_form', successful_form, name="successful_form"),
]
