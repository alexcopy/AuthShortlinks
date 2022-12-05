from django.shortcuts import render

# Create your views here.


def cams(request):
    return render(request, 'cams.html', {})

def meters(request):
    return render(request, 'meters.html', {})