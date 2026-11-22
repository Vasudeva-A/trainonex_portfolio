from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.project_list, name="projects"),
    path("projects/add/", views.project_create, name="project_add"),
    path("projects/<int:project_id>/edit/", views.project_edit, name="project_edit"),
    path("projects/<int:project_id>/delete/", views.project_delete, name="project_delete"),
    path("categories/", views.category_list, name="categories"),
    path("categories/<int:category_id>/delete/", views.category_delete, name="category_delete"),
]
