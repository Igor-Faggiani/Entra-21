from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", views.create, name="create"),
    path("<int:id>/delete", views.delete, name="delete"),
    path("search", views.search, name="search"),
    path("<int:id>/toggle_enabled", views.toggle_enabled, name="toggle_enabled"),
    path("categorias/", views.get_categories, name="categories"),
    path("categorias/cadastro/", views.create_category, name="categories_create"),
    path("categorias/<int:id>/delete", views.delete_category, name="category_delete"),
    path("categorias/search", views.search_categories, name="categories_search"),
    path("categorias/<slug:slug>/", views.update_category, name="categories_update"),
    path("<slug:slug>/", views.update, name="update"),
]
