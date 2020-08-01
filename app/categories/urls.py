from django.urls import path

from categories.views import GetCategoriesView

urlpatterns = [
    path("", GetCategoriesView.as_view(), name="get-categories"),
]