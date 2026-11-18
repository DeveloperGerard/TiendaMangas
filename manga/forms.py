from django import forms

from .models import Manga


class MangaForm(forms.ModelForm):
    fecha_publicacion = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}, format="%Y-%m-%d"),
    )

    class Meta:
        model = Manga
        fields = (
            "isbn",
            "titulo",
            "autor",
            "precio",
            "stock_copias",
            "disponible",
            "fecha_publicacion",
            "genero",
        )
        widgets = {
            "isbn": forms.TextInput(attrs={"class": "form-control"}),
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "autor": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
            "stock_copias": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
            "disponible": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "genero": forms.Select(attrs={"class": "form-select"}),
        }