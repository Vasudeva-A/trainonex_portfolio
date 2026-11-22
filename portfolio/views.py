from django.shortcuts import render, get_object_or_404
from .models import Project, Category


def project_list(request):
    projects = Project.objects.filter(is_published=True).select_related("category")
    categories = Category.objects.all()
    selected_category = request.GET.get("category", "")
    if selected_category:
        projects = projects.filter(category__slug=selected_category)
    return render(request, "portfolio/project_list.html", {
        "projects": projects,
        "categories": categories,
        "selected_category": selected_category,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_published=True)
    return render(request, "portfolio/project_detail.html", {"project": project})
