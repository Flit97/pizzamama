from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


def index(request):
    '''pizzas = Pizza.objects.all()
    pizza_names_and_price = [pizza.nom + " : " + str(pizza.prix) + "€" for pizza in pizzas]
    pizza_names_string = ", ".join(pizza_names_and_price)
    return HttpResponse("Les pizzas : " + pizza_names_string)'''
    return render(request, 'menu/index.htm')


