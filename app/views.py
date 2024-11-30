from django.shortcuts import render


def snow(request):
    return render(request, 'app/snow.html')


def project(request):
    return render(request, 'app/project.html')


def bio(request):
    return render(request, 'app/bio.html')
