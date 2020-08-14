from django.shortcuts import render


def index(request):
    return render(request, 'frontend/react-frontend/public/index.html')