from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'oro/index.html')
# def home(request):
#     return render (request, 'oro/home.html')
def organisationchart(request):
    return render (request, 'oro/organisationchart.html')
def events(request):
    return render (request, 'oro/event.html')
def gallery(request):
    return render (request, 'oro/gallery.html')
def about(request):
    return render (request, 'oro/about.html')
def contactus(request):
    return render (request, 'oro/contact.html')