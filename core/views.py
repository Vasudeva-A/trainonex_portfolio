from django.shortcuts import render
from portfolio.models import Project


def home(request):
    projects = Project.objects.filter(is_published=True).select_related("category")[:6]
    return render(request, "core/home.html", {"projects": projects})


def about(request):
    return render(request, "core/about.html")


def services(request):
    return render(request, "core/services.html")
