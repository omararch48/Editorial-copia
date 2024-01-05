from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def us(request):
    return render(request, 'core/us.html')


def howto(request):
    return render(request, 'core/howto.html')


def blog(request):
    return render(request, 'core/blog.html')


def contact(request):
    return render(request, 'core/contact.html')