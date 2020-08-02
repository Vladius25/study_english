from django.urls import path

from words.views import GetWordView

urlpatterns = [
    path("<int:pk>/", GetWordView.as_view(), name="get-word"),
]