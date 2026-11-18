from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import MangaForm
from .models import Manga


class MangaLista(LoginRequiredMixin, ListView):
    model = Manga
    template_name = "mangas.html"
    context_object_name = "mangas"


class MangaDetalle(LoginRequiredMixin, DetailView):
    model = Manga
    template_name = "detalle_manga.html"
    context_object_name = "manga"


class MangaCrear(LoginRequiredMixin, CreateView):
    model = Manga
    form_class = MangaForm
    template_name = "manga_form.html"
    success_url = reverse_lazy("inicio")


class MangaActualizar(LoginRequiredMixin, UpdateView):
    model = Manga
    form_class = MangaForm
    template_name = "manga_form.html"
    success_url = reverse_lazy("inicio")


class MangaEliminar(LoginRequiredMixin, DeleteView):
    model = Manga
    template_name = "manga_confirm_delete.html"
    context_object_name = "manga"
    success_url = reverse_lazy("inicio")


