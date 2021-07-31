from django.shortcuts import render

def index(request):
    return render(request, 'shorturlsapp/index.html')

def reports(request):
    return render(request, 'shorturlsapp/reports.html')


# Create your views here.
