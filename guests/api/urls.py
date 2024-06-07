from django.urls import path

from guests.api import views

urlpatterns = [
    path(
        "get-entries-list", views.EntriesListView.as_view(), name="api-get-entries-list"
    ),
    path("get-users-list", views.UsersListView.as_view(), name="api-get-users-list"),
    path("create-user", views.EntryCreateView.as_view(), name="api-create-user"),
    path(
        "kwargs-deneme/<str:data>",
        views.UrlDataView.as_view(),
        name="api-kwargs-deneme",
    ),
]
