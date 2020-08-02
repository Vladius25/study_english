from django.urls import path

from themes.views import GetThemeView, GetThemesView

urlpatterns = [
    path("", GetThemesView.as_view(), name="get-themes"),
    path("<int:pk>/", GetThemeView.as_view(), name="get-theme")
]
