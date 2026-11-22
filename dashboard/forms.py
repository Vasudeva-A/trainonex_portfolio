from django import forms
from portfolio.models import Project, Category


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title", "category", "short_description", "description",
            "cover_image", "project_url", "github_url", "is_published",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 6, "class": "form-control"}),
            "short_description": forms.Textarea(attrs={"rows": 2, "class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "cover_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "project_url": forms.URLInput(attrs={"class": "form-control"}),
            "github_url": forms.URLInput(attrs={"class": "form-control"}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
