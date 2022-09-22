from django.shortcuts import render

"""
def index(request):
    return HttpResponse("<h2>Главная</h2>")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
"""


def index(request):
   # return HttpResponse("Hello METANIT.COM")
    return render(request, "index.html")
def contacts(request):
    return render(request, "contacts.html")