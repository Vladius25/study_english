from django.urls import path

from levels.views import GetLevelsView

urlpatterns = [
    path("", GetLevelsView.as_view(), name="get-levels"),
]