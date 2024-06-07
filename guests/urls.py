from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create-entry/", views.create_entry, name="create-entry"),
    path("entries-list/", views.entries_list, name="entries-list"),
    path("user-data/<str:pk>/", views.get_user_data, name="user-data"),
    path("users-list/", views.users_list, name="users-list"),
]
