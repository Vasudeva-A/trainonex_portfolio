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
            "description": forms.Textarea(attrs={"rows": 6}),
            "short_description": forms.Textarea(attrs={"rows": 2}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
