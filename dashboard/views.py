from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from portfolio.models import Project, Category
from .forms import ProjectForm, CategoryForm


@staff_member_required
def home(request):
    return render(request, "dashboard/home.html", {
        "project_count": Project.objects.count(),
        "published_count": Project.objects.filter(is_published=True).count(),
        "category_count": Category.objects.count(),
        "projects": Project.objects.select_related("category")[:8],
    })


@staff_member_required
def project_list(request):
    projects = Project.objects.select_related("category")
    return render(request, "dashboard/project_list.html", {"projects": projects})


@staff_member_required
def project_create(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project added successfully.")
        return redirect("dashboard:projects")
    return render(request, "dashboard/project_form.html", {"form": form, "page_title": "Add project"})


@staff_member_required
def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project updated successfully.")
        return redirect("dashboard:projects")
    return render(request, "dashboard/project_form.html", {"form": form, "page_title": "Edit project"})


@staff_member_required
def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted.")
        return redirect("dashboard:projects")
    return render(request, "dashboard/project_confirm_delete.html", {"project": project})


@staff_member_required
def category_list(request):
    categories = Category.objects.all()
    form = CategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Category added.")
        return redirect("dashboard:categories")
    return render(request, "dashboard/categories.html", {"categories": categories, "form": form})


@staff_member_required
def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Category deleted.")
    return redirect("dashboard:categories")
