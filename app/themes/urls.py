from django.urls import path

from themes.views import GetThemeView

urlpatterns = [
    path("<int:pk>/", GetThemeView.as_view(), name="get-theme")
]
