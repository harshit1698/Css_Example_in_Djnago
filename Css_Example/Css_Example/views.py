from django.shortcuts import render


def Show(request):
    return render(request,"h1.html")

def Home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")