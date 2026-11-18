from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("accounts/login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("", views.MangaLista.as_view(), name="home"),
    path("manga/", views.MangaLista.as_view(), name="inicio"),
    path("manga/crear/", views.MangaCrear.as_view(), name="crearManga"),
    path("manga/<int:pk>/editar/", views.MangaActualizar.as_view(), name="editarManga"),
    path("manga/<int:pk>/eliminar/", views.MangaEliminar.as_view(), name="eliminarManga"),
    path("manga/<int:pk>/", views.MangaDetalle.as_view(), name="detalleManga"),
]
