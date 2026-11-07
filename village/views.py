from django.shortcuts import render

def accueil(request):
    return render(request, 'village/accueil.html')

def histoire(request):
    return render(request, 'village/histoire.html')

def patrimoine(request):
    return render(request, 'village/patrimoine.html')

def culture(request):
    return render(request, 'village/culture.html')

def galerie(request):
    return render(request, 'village/galerie.html')

def contact(request):
    return render(request, 'village/contact.html')
