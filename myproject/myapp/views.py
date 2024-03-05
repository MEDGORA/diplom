from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse
import logging
from .forms import InvocationForm
from .models import Invocation, Сonsumer, New, Personal, Vacancy

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    logger.info("Home page accessed")
    return render(request, "myapp/home.html")

def about(request):
    logger.info("About page accessed")
    return render(request, "myapp/about.html")

def vacansies(request):
    logger.info("Vacansies page accessed")
    vacansies = get_list_or_404(Vacancy)
    return render(request, 'myapp/vacansies.html', {'vacansies': vacansies})

def personal(request):
    logger.info("Personal page accessed")
    personals = get_list_or_404(Personal)
    return render(request, 'myapp/personal.html', {'personals': personals})

def news(request):
    logger.info("News page accessed")
    news = get_list_or_404(New)
    return render(request, 'myapp/news.html', {'news': news})

def for_consumers(request):
    logger.info("For_consumers page accessed")
    return render(request, "myapp/for_consumers.html")

def contacts(request):
    logger.info("Contacts page accessed")
    return render(request, "myapp/contacts.html")

def requisites(request):
    logger.info("Requisites page accessed")
    return render(request, "myapp/requisites.html")

def successful_form(request):
    logger.info("Successful_form page accessed")
    return render(request, "myapp/successful_form.html")

def form(request):
    if request.method == "POST":
        form = InvocationForm(request.POST, request.FILES)
        message = "Ошибка данных"
        if form.is_valid(): #and hash(password) == hash()
            name = form.cleaned_data["name"]
            second_name = form.cleaned_data["second_name"]
            last_name = form.cleaned_data["last_name"]
            address = form.cleaned_data["address"]
            personal_account = form.cleaned_data["personal_account"]
            description = form.cleaned_data["description"]
            if Сonsumer.objects.filter(name=name, second_name=second_name, last_name=last_name, personal_account=personal_account).exists() == True:
                invocation = Invocation(name=name, second_name=second_name, last_name=last_name , address=address, personal_account=personal_account, description=description)
                invocation.save()
                #message = "Новое обращение успешно создано"
                logger.info(f"Добавили в базу данных Invocation: адресс: {address}, обращение: {description}")
                return render(request, "myapp/successful_form.html")
            elif Сonsumer.objects.filter(name=name, second_name=second_name, last_name=last_name, personal_account=personal_account).exists() == False:
                form = InvocationForm()  
                message = "Личный счёт введён неверно"
    else:
        form = InvocationForm()  
        message = "Заполните форму"
    return render(request, 'myapp/form.html', {'form': form, 'message': message})