import requests
from django.shortcuts import render

# Create your views here.
from .services import pondtemp_services


def cams(request):
    cams_data = pondtemp_services.all_cams_index()
    return render(request, 'cams.html', {'cams': cams_data})


def meters(request):
    return render(request, 'meters.html', {})


def cams_harvest_details(request):
    page_content = pondtemp_services.single_cam_details(request)

    return render(request, 'cams_details.html', {'pictures': page_content['data'], 'pagination': page_content})
