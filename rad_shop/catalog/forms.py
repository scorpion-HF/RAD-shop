from django import forms
from .models import Category


class CategoryFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        for category in categories:
            self.fields[category.title] = forms.BooleanField(
                label=category.title,
                required=False,
                widget=forms.CheckboxInput(
                    attrs={'class': "form-check-input me-1", 'value': category.pk}
            ))

